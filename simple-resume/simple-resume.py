from pylatex import Document, Section, Subsection, Command, UnsafeCommand
from pylatex.base_classes import Environment, CommandBase, Arguments
from pylatex.package import Package
from pylatex.utils import NoEscape, italic


class ExampleEnvironment(Environment):
    """
    A class representing a custom LaTeX environment.
    This class represents a custom LaTeX environment named
    ``exampleEnvironment``.
    """

    _latex_name = 'exampleEnvironment'
    packages = [
                Package('mdframed'),
                Package('babel', options="english"),
                #Package('inputenc'), #Already added by pylatex
                Package('microtype', options ="protrusion=true,expansion=true"),
                Package('amsmath'),
                Package('amsfonts'),
                Package('amsthm'),
                Package('graphicx'),
                Package('xcolor', options="svgnames"),
                Package('geometry'),
                Package('url'),
                Package('sectsty')]


# class ExampleCommand(CommandBase):
#     """
#     A class representing a custom LaTeX command.
#     This class represents a custom LaTeX command named
#     ``exampleCommand``.
#     """

#     _latex_name = 'exampleCommand'
#     packages = [Package('graphicx')]

#\sepspace
class SepSpace(CommandBase):
    """
    A class representing a custom LaTeX command.
    This class represents a custom LaTeX command named
    ``exampleCommand``.
    """
#\newcommand{\sepspace}{\vspace*{1em}}
    _latex_name = 'sepspace'
#    packages = [('graphicx')]

#\MyName
class MyName(CommandBase):
    """
    A class representing a custom LaTeX command.
    This class represents a custom LaTeX command named
    ``exampleCommand``.
    """
# { % Name
# 		\Huge \usefont{OT1}{phv}{b}{n} \hfill #1
# 		\par \normalsize \normalfont}


    _latex_name = 'MyName'
#   packages = [Package('graphicx')]


#\MySlogan
class MySlogan(CommandBase):
    """
    A class representing a custom LaTeX command.
    This class represents a custom LaTeX command named
    ``exampleCommand``.
    """
# \newcommand{\MySlogan}[1]{ % Slogan (optional)
# 		\large \usefont{OT1}{phv}{m}{n}\hfill \textit{#1}
# 		\par \normalsize \normalfont}


    _latex_name = 'MySlogan'
#    packages = [Package('graphicx')]


#\NewPart
class NewPart(CommandBase):
    """
    A class representing a custom LaTeX command.
    This class represents a custom LaTeX command named
    ``exampleCommand``.
    """

    _latex_name = 'NewPart'
#    packages = [Package('graphicx')]


#\PersonalEntry
class PersonalEntry(CommandBase):
    """
    A class representing a custom LaTeX command.
    This class represents a custom LaTeX command named
    ``exampleCommand``.
    """
# \newcommand{\PersonalEntry}[2]{
# 		\noindent\hangindent=2em\hangafter=0 % Indentation
# 		\parbox{\spacebox}{        % Box to align text
# 		\textit{#1}}		       % Entry name (birth, address, etc.)
# 		\hspace{1.5em} #2 \par}    % Entry value

    _latex_name = 'PersonalEntry'
#    packages = [Package('graphicx')]


#\SkillsEntry
class SkillsEntry(CommandBase):
    """
    A class representing a custom LaTeX command.
    This class represents a custom LaTeX command named
    ``exampleCommand``.
    """
#       \newcommand{\SkillsEntry}[2]{      % Same as \PersonalEntry
# 		\noindent\hangindent=2em\hangafter=0 % Indentation
# 		\parbox{\spacebox}{        % Box to align text
# 		\textit{#1}}			   % Entry name (birth, address, etc.)
# 		\hspace{1.5em} #2 \par}    % Entry value


    _latex_name = 'SkillsEntry'
#    packages = [Package('graphicx')]


#\EducationEntry
class EducationEntry(CommandBase):
    """
    A class representing a custom LaTeX command.
    This class represents a custom LaTeX command named
    ``exampleCommand``.
    """

    _latex_name = 'EducationEntry'
#    packages = [Package('graphicx')]


#\WorkEntry
class WorkEntry(CommandBase):
    """
    A class representing a custom LaTeX command.
    This class represents a custom LaTeX command named
    ``exampleCommand``.
    """

    _latex_name = 'WorkEntry'
#    packages = [Package('graphicx')]




#\PersonalEntry
class PersonalEntry(CommandBase):
    """
    A class representing a custom LaTeX command.
    This class represents a custom LaTeX command named
    ``exampleCommand``.
    """

    _latex_name = 'PersonalEntry'
#    packages = [Package('graphicx')]








def fill_document(doc):
    """Add a section, a subsection and some text to the document.

    :param doc: the document
    :type doc: :class:`pylatex.document.Document` instance
    """
    with doc.create(Section('Experience')):
        doc.append('Company 1 ')
        doc.append(italic('italic text. '))

        with doc.create(Subsection('Company 2')):
            doc.append('Also some crazy characters: $&#{}')


if __name__ == '__main__':
    # Basic document
    #doc = Document('simple')
    #fill_document(doc)

#    doc.generate_pdf(clean_tex=False)
#   doc.generate_tex()

    # Document with `\maketitle` command activated
    #doc = Document()
    doc = Document(documentclass = 'scrartcl' , document_options = ["paper=a4","fontsize=11pt"])

    doc.preamble.append(Command('title', 'Resumee'))
    doc.preamble.append(Command('author', 'Abhinav Sharma'))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.append(NoEscape(r'\maketitle'))

    fill_document(doc)

   # doc.generate_pdf('basic_maketitle', clean_tex=False)


   # # Define the new command
   #  new_comm = UnsafeCommand('newcommand', '\exampleCommand', options=3,
   #                           extra_arguments=r'\color{#1} #2 #3 \color{black}')
   #  doc.append(new_comm)

############ MACROS

#\newcommand{\sepspace}{\vspace*{1em}}
    sepspace = UnsafeCommand('newcommand', r'\sepspace', options=0,
                             extra_arguments=r'\vspace*{1em}')
    doc.append(sepspace)

# { % Name
# 		\Huge \usefont{OT1}{phv}{b}{n} \hfill #1
# 		\par \normalsize \normalfont}

    MyName = UnsafeCommand('newcommand', r'\MyName', options=1,
                             extra_arguments=r'\Huge\usefont{OT1}{phv}{b}{n}\hfill{#1}\par\normalsize\normalfont')
    doc.append(MyName)

# \newcommand{\MySlogan}[1]{ % Slogan (optional)
# 		\large \usefont{OT1}{phv}{m}{n}\hfill \textit{#1}
# 		\par \normalsize \normalfont}
    MySlogan = UnsafeCommand('newcommand', r'\MySlogan', options=1,
                             extra_arguments=r"""
                             \large\usefont{OT1}{phv}{m}{n}\hfill\textit{#1}\par\normalsize\normalfont

 """)


    doc.append(MySlogan)



    NewPart = UnsafeCommand('newcommand', r'\NewPart', options=1,
                             extra_arguments=r"""\section*{\uppercase{#1}}""")

    doc.append(NewPart)

# \newcommand{\PersonalEntry}[2]{
# 		\noindent\hangindent=2em\hangafter=0 % Indentation
# 		\parbox{\spacebox}{        % Box to align text
# 		\textit{#1}}		       % Entry name (birth, address, etc.)
# 		\hspace{1.5em} #2 \par}    % Entry value


    PersonalEntry = UnsafeCommand('newcommand', r'\PersonalEntry', options=2,
                             extra_arguments=r"""
        \noindent\hangindent=2em\hangafter=0 % Indentation
		\parbox{\spacebox}{        % Box to align text
		\textit{#1}}		       % Entry name (birth, address, etc.)
		\hspace{1.5em} #2 \par}    % Entry value

 """)

    doc.append(PersonalEntry)

#       \newcommand{\SkillsEntry}[2]{      % Same as \PersonalEntry
# 		\noindent\hangindent=2em\hangafter=0 % Indentation
# 		\parbox{\spacebox}{        % Box to align text
# 		\textit{#1}}			   % Entry name (birth, address, etc.)
# 		\hspace{1.5em} #2 \par}    % Entry value

    SkillsEntry = UnsafeCommand('newcommand', r'\SkillsEntry', options=2,
                             extra_arguments=r"""

		\noindent\hangindent=2em\hangafter=0 % Indentation
		\parbox{\spacebox}{        % Box to align text
		\textit{#1}}			   % Entry name (birth, address, etc.)
		\hspace{1.5em} #2 \par    % Entry value

""")

    doc.append(SkillsEntry)

    EducationEntry = UnsafeCommand('newcommand', r'\EducationEntry', options=2,
                             extra_arguments=r"""
		\noindent \textbf{#1} \hfill      % Study
		\colorbox{Black}{%
			\parbox{6em}{%
			\hfill\color{White}#2}} \par  % Duration
		\noindent \textit{#3} \par        % School
		\noindent\hangindent=2em\hangafter=0 \small #4 % Description
		\normalsize \par

 """)

    doc.append(EducationEntry)





    WorkEntry = UnsafeCommand('newcommand', r'\WorkEntry', options=2,
                             extra_arguments=r"""
         % Same as \EducationEntry
		\noindent \textbf{#1} \hfill      % Jobname
		\colorbox{Black}{\color{White}#2} \par  % Duration
		\noindent \textit{#3} \par              % Company
		\noindent\hangindent=2em\hangafter=0 \small #4 % Description
		\normalsize \par
 """)

    doc.append(WorkEntry)





    # # Use our newly created command with different arguments
    # doc.append(ExampleCommand(arguments=Arguments('blue', 'Hello', 'World!')))
    # doc.append(ExampleCommand(arguments=Arguments('green', 'Hello', 'World!')))
    # doc.append(ExampleCommand(arguments=Arguments('red', 'Hello', 'World!')))




    # Add stuff to the document
    with doc.create(Section('Experience')):
        doc.append('Some text.')


    # Define a style for our box
    mdf_style_definition = UnsafeCommand('mdfdefinestyle',
                                         arguments=['my_style',
                                                    ('linecolor=#1,'
                                                     'linewidth=#2,'
                                                     'leftmargin=1cm,'
                                                     'leftmargin=1cm')])



    # Define the new environment using the style definition above
    new_env = UnsafeCommand('newenvironment', 'exampleEnvironment', options=2,
                            extra_arguments=[
                                mdf_style_definition.dumps() +
                                r'\begin{mdframed}[style=my_style]',
                                r'\end{mdframed}'])
    doc.append(new_env)

    # Usage of the newly created environment
    with doc.create(
            ExampleEnvironment(arguments=Arguments('red', 3))) as environment:
        environment.append('This is the actual content')


#    doc.generate_pdf('basic_maketitle2', clean_tex=False)
    tex = doc.dumps()  # The document as string in LaTeX syntax
    doc.generate_tex("./simple-resume")
