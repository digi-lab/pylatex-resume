from pylatex import Document, Section, Subsection, Command, Itemize
from pylatex.utils import italic, NoEscape


def fill_document(doc):
    """Add a section, a subsection and some text to the document.

    :param doc: the document
    :type doc: :class:`pylatex.document.Document` instance
    """
    with doc.create(Section('Experience')):

        with doc.create(Subsection('Fourtek (IT) Solutions Pvt. Ltd.')):
            doc.append(italic('Software Engineer - AI/ML'))

        with doc.create(Subsection('Cyber Indian App Stores Pvt. Ltd.')):
            doc.append('Chief Technology Officer')

    with doc.create(Section('Publications')):

        with doc.create(Subsection('Research on Tuberculosis')):
            doc.append(italic('Shell Scripting'))

    with doc.create(Section('"Itemize" list')):
        with doc.create(Itemize()) as itemize:
            itemize.add_item("the first item")
            itemize.add_item("the second item")
            itemize.add_item("the third etc")
            # you can append to existing items
            itemize.append(Command("ldots"))




# Basic document
doc = Document('resume')
fill_document(doc)

#doc.generate_pdf(clean_tex=False)
#doc.generate_tex()

# Document with `\maketitle` command activated
doc = Document()

doc.preamble.append(Command('title', 'Resumee'))
doc.preamble.append(Command('author', 'Abhinav Sharma'))
doc.preamble.append(Command('date', NoEscape(r'\today')))
doc.append(NoEscape(r'\maketitle'))

fill_document(doc)

#doc.generate_pdf('basic_maketitle', clean_tex=False)

# Add stuff to the document
with doc.create(Section('Experience')):
    doc.append('Some text.')

#doc.generate_pdf('basic_maketitle2', clean_tex=False)
tex = doc.dumps()  # The document as string in LaTeX syntax
doc.generate_tex("./abhi18av")

