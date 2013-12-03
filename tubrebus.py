#!/usr/bin/python
# -*- coding: utf-8 -*-

testWords = [
    "Abrahamsberg",
    "Akalla",
    "Åkeshov",
    "Alby",
    "Alvik",
    "Ängbyplan",
    "Aspudden",
    "Axelsberg",
    "Bagarmossen",
    "Bandhagen",
    "Bergshamra",
    "Björkhagen",
    "Blackeberg",
    "Blåsut",
    "Bredäng",
    "Brommaplan",
    "Danderyds sjukhus",
    "Duvbo",
    "Enskede gård",
    "Farsta",
    "Farsta strand",
    "Fittja",
    "Fruängen",
    "Fridhemsplan",
    "Gamla stan",
    "Gärdet",
    "Globen",
    "Gubbängen",
    "Gullmarsplan",
    "Hagsätra",
    "Hägerstensåsen",
    "Hallonbergen",
    "Hallunda",
    "Hammarbyhöjden",
    "Hässelby Gård",
    "Hässelby Strand",
    "Hjulsta",
    "Högdalen",
    "Hökarängen",
    "Hornstull",
    "Hötorget",
    "Husby",
    "Huvudsta",
    "Islandstorget",
    "Johannelund",
    "Karlaplan",
    "Kärrtorp",
    "Kista",
    "Kristineberg",
    "Kungsträdgården",
    "Liljeholmen",
    #"Mälarhöjden",
    "Mariatorget",
    "Masmo",
    "Medborgarplatsen",
    "Midsommarkransen",
    "Mörby centrum",
    "Näckrosen",
    "Norsborg",
    "Odenplan",
    "Örnsberg",
    "Östermalmstorg",
    "Råcksta",
    "Rådhuset",
    "Rådmansgatan",
    "Rågsved",
    "Rinkeby",
    # "Rissne",
    "Ropsten",
    "Sandsborg",
    "Sätra",
    "Skanstull",
    "Skärholmen",
    "Skärmarbrink",
    "Skarpnäck",
    "Skogskyrkogården",
    "Slussen",
    "Sockenplan",
    "Solna centrum",
    "Sankt Eriksplan",
    "Stadion",
    "Stadshagen",
    "Stora Mossen",
    "Stureby",
    "Sundbybergs centrum",
    "Svedmyra",
    "T-Centralen",
    "Tallkrogen",
    "Tekniska högskolan",
    "Telefonplan",
    "Tensta",
    "Thorildsplan",
    "Universitetet",
    "Vällingby",
    "Vårberg",
    "Vårby gård",
    "Västertorp",
    "Västra skogen",
    "Vreten",
    "Zinkensdamm",
]

skip = [
    "s", "-", "n", "e", "d", "t"
]

words = [
    "frid", "hem", "plan", "rop", "sten", "telefon", "gull", "mars", "horn", "tull", "oden", "vik",
    "mör", "by", "strand", "al", "by", "blås", "ut", "en", "sked", "hö", "torget", "råd", "man", "äng", "by",
    "gatan", "berg", "midsommar", "asp", "axel", "hallon", "skarp", "näck", "oden", "central", "centrum", "udde",
    "krans", "t", "stan", "gamla", "kung", "trädgård", "skog", "kyrkogård", "abraham", "kall", "a", "hov", "åke",
    "bagar", "moss", "band", "hage", "hamra", "hage", "björk", "b", "lack", "bred", "bro", "mma", "sjukhus", "dan",
    "de", "ry", "duv", "bo", "gård", "vår", "välling", "thorild", "teknisk", "hög", "skola", "tall", "krog", "myra",
    "zink", "damm", "far", "sta", "huvud", "fitt", "ja", "fru", "gärde", "glo", "ben", "gubb", "hag", "sätra",
    "häger", "ås", "ny", "hal", "lund", "hammar", "höjd", "hjul", "västra", "vrete", "socken", "sluss", "maria", "torg",
    "mas", "mo", "hässel", "hög", "dal", "hökar", "hus", "island", "jo", "hann", "lund", "karla", "kärr", "torp",
    "kista", "kristin", "lilje", "holme", "plats", "medborgar", "ros", "nors", "borg", "örn", "öster", "malm", "rå",
    "ck", "råg", "sved", "rink", "sand", "sture", "skans", "skär", "skärmar", "brink", "sol", "na", "sankt", "erik",
    "stad", "i", "on", "stora", "moss", "sund", "universitetet", "väster"
]


class WordParser:

    def parseSingle(self, word, lookupList):
        while word != "":

            if word in lookupList:
                return word

            word = word[:-1]

        return False

    def parse(self, word):
        parts = []
        word = "".join(word.split()).lower()  # strips all whitespace and converts to lowercase
        word = word.replace("Å", "å").replace("Ä", "ä").replace("Ö", "ö")

        while word != "":
            work = self.parseSingle(word, words)

            if not work:
                skipWork = self.parseSingle(word, skip)

                if not skipWork:
                    raise RuntimeError("Failed to lookup word '{0}'".format(word))

                else:
                    word = word[len(skipWork):]
                    continue

            else:
                word = word[len(work):]
                parts.append(work)

        return parts

if __name__ == '__main__':
    parser = WordParser()

    for t in testWords:
        print "{0}: {1}".format(t, parser.parse(t))