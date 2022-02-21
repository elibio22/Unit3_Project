import sqlite3

import flask
from flask import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/transcript/<transcript_id>/<sh_rna>', methods=['GET'])
def transcript(transcript_id, sh_rna):
    connection = sqlite3.connect("human.db")
    # connection.row_factory = dict_factory
    cursor = connection.cursor()
    row = cursor.execute("SELECT transcript FROM transcripts where id = ?", (transcript_id,)).fetchone()
    if len(row) == 0:
        return "Record not found", 400

    transcript = row[0]

    primers = find_all(transcript)

    filtered = []
    for primer in primers:
        content = transcript[primer["content"]["start"]:primer["content"]["end"]]
        if content.find(sh_rna) != -1:
            filtered.append(primer)

    response = app.response_class(
        response=json.dumps(filtered),
        status=200,
        mimetype='application/json'
    )
    return response


def melting_temperature(primer):
    temp = 0
    for nucl in primer:
        if nucl == 'C' or nucl == 'G':
            temp += 4
        if nucl == 'A' or nucl == 'T':
            temp += 2
    return temp


def gc_content(primer):
    count = 0
    for nucl in primer:
        if nucl == 'C' or nucl == 'G':
            count += 1
    return count / len(primer)


def valid_primer(primer):
    # Starts with 1-2 G/C pairs
    if not primer[0] in ['C', 'G']:
        return False

    # Ends with 1-2 G/C pairs
    if not primer[-1] in ['C', 'G']:
        return False

    # G/C content = 40%-60%
    gc_ratio = gc_content(primer)
    if gc_ratio < 0.4 or gc_ratio > 0.6:
        return False

    # Melting temperature (Tm) of 50-60°C
    temp = melting_temperature(primer)
    if temp < 50 or temp > 60:
        return False

    return True


def valid_primers_pair(primer1, primer2):
    temp1 = melting_temperature(primer1)
    temp2 = melting_temperature(primer2)
    return abs(temp1 - temp2) <= 5


def find_all(transcript, content_size=70):
    primers = []
    for i in range(len(transcript) // 2):
        try:
            for size1 in range(18, 24):
                for_primer = transcript[i:i + size1]
                if not valid_primer(for_primer):
                    raise Exception()

                for j in range(i + len(for_primer) + content_size, len(transcript) - 18):
                    for size2 in range(18, 24):
                        rev_primer = transcript[j:j + size2]
                        if not valid_primer(rev_primer):
                            raise Exception()

                        if not valid_primers_pair(for_primer, rev_primer):
                            raise Exception()

                        primers.append({
                            "forward": {
                                "start": i,
                                "length": len(for_primer),
                                "seq": for_primer,
                            },
                            "reverse": {
                                "start": j,
                                "length": len(rev_primer),
                                "seq": rev_primer,
                            },
                            "content": {
                                "start": i + len(for_primer),
                                "end": j,
                                "length": j - i - len(for_primer),
                            },
                        })
                        raise Exception()
        except Exception:
            continue
    return primers


if __name__ == '__main__':
    app.run()
