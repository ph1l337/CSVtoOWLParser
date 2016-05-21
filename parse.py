import csv


def main(csvfile):
    with open(csvfile) as csvfile:
        with open('out.owl', 'w+') as out:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                out_string = "<owl:Class rdf:about=\"http://www.semanticweb.org/IAyPE/EducationMapptin/SourceGermany#{}\">\n"\
                             "<rdfs:subClassOf rdf:resource=\"http://www.semanticweb.org/IAyPE/EducationMapptin/SourceGermany#Subject\"/>\n"\
                             "</owl:Class>\n".format(row['Subject'].replace(' ', '_'))
                out.write(out_string)


if __name__ == '__main__':
    csvfile = 'germany_students_enrolled.csv'
    main(csvfile)
