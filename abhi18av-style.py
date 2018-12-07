import json, os, sys
from pylatex.base_classes import Environment, CommandBase, Arguments
from pylatex.package import Package
from pylatex import Document, Section, Subsection, Command, UnsafeCommand
from pylatex.utils import NoEscape, italic






if __name__ == '__main__':

    doc = Document()


    doc.preamble.append(Command("NeedsTeXFormat", "LaTeX2e"))

#    doc.preamble.append(Command("ProvidesPackage", "style", ["2014/08/24 Example LaTeX package"]))
    doc.preamble.append(Command("ProvidesPackage", "style"))

    doc.preamble.append(Command("usepackage", "mdframed"))
    doc.preamble.append(Command("usepackage", "babel","english"))
#    doc.preamble.append(Command("usepackage", "inputenc","utf8x"))
    doc.preamble.append(Command("usepackage","microtype", ["protrusion=true" , "expansion=true"]))
    doc.preamble.append(Command("usepackage", "amsmath"))
    doc.preamble.append(Command("usepackage", "amsfonts"))
    doc.preamble.append(Command("usepackage", "amsthm"))
    doc.preamble.append(Command("usepackage", "graphicx"))
    doc.preamble.append(Command("usepackage", "xcolor", "svgnames"))
    doc.preamble.append(Command("usepackage", "geometry"))
    doc.preamble.append(Command("usepackage", "url"))
    doc.preamble.append(Command("usepackage", "sectsty"))


    tex = doc.dumps()  # The document as string in LaTeX syntax

    doc.generate_tex("./abhi18av-style")

    # NOTE to delete the 1st and last 3 lines of the generated style file
    # this is important to take care of the \document \begin \end parts
    readFile = open("./abhi18av-style.tex")
    lines = readFile.readlines()
    readFile.close()

    w = open("./abhi18av-style.tex",'w')
    w.writelines([item for item in lines[1 :-3]])
    w.close()
