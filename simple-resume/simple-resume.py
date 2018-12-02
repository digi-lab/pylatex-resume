from pylatex.base_classes import Environment, CommandBase, Arguments
from pylatex.package import Package
from pylatex import Document, Section, Subsection, Command, UnsafeCommand
from pylatex.utils import NoEscape, italic


class ResumeEnvironment(Environment):
    """
    A class representing a custom LaTeX environment.
    This class represents a custom LaTeX environment named
    ``resumeEnvironment``.
    """

    _latex_name = 'resumeEnvironment'
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



#######################################

class MyName(CommandBase):
    _latex_name = 'MyName'

class MySlogan(CommandBase):
    _latex_name = 'MySlogan'

class NewPart(CommandBase):
    _latex_name = 'NewPart'

class PersonalEntry(CommandBase):
    _latex_name = 'PersonalEntry'

class SkillsEntry(CommandBase):
    _latex_name = 'SkillsEntry'

class EducationEntry(CommandBase):
    _latex_name = 'EducationEntry'

class WorkEntry(CommandBase):
    _latex_name = 'WorkEntry'


#######################################





if __name__ == '__main__':


    doc = Document(documentclass = 'scrartcl' , document_options = ["paper=a4","fontsize=11pt"])


    doc.preamble.append(Command('title', 'Resumee'))
    doc.preamble.append(Command('author', 'Abhinav Sharma'))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.append(NoEscape(r'\maketitle'))

    with doc.create(Section('Experience')):
        doc.append('Cyber Indian App Stores Pvt. Ltd.')
        doc.append(italic('Chief Technology Officer'))

        with doc.create(Subsection('Fourtek (IT) Solutions Pvt. Ltd.')):
            doc.append('Software Engineer AI/ML')
###########################

###########################


        ########
# TODO: Learn how to deal with environments
    # Define the new environment using the style definition above
    new_env = UnsafeCommand('newenvironment', 'resumeEnvironment', options=2,
                            extra_arguments=[
                                r"""\begin{mdframed}[style=my_style]""",
                                r"""\end{mdframed}"""])
    doc.append(new_env)

    # Usage of the newly created environment
    with doc.create(
            ResumeEnvironment(arguments=Arguments('red', 3))) as environment:
        environment.append('\nThis is the actual content\n')

        ########

###########################

###########################

    # # Use our newly created command with different arguments
    # doc.append(ExampleCommand(arguments=Arguments('blue', 'Hello', 'World!')))





    sepspace = UnsafeCommand('newcommand', r'\sepspace',
                             extra_arguments=r"""
                             \vspace*{1em}
""")

    doc.append(sepspace)


###########################

###########################


    MyName = UnsafeCommand('newcommand', r'\MyName', options=1,
                             extra_arguments=r"""
    		\Huge \usefont{OT1}{phv}{b}{n} \hfill #1
     		\par \normalsize \normalfont
""")

    doc.append(MyName)


#    doc.append(MyName(arguments=Arguments("Abhinav Sharma")))



###########################

###########################



    MySlogan = UnsafeCommand('newcommand', r'\MySlogan', options=1,
                             extra_arguments=r"""
  		\large \usefont{OT1}{phv}{m}{n}\hfill \textit{#1}
		\par \normalsize \normalfont
""")


    doc.append(MySlogan)


    NewPart = UnsafeCommand('newcommand', r'\NewPart', options=1,
                             extra_arguments=r"""
                             \section*{\uppercase{#1}}
""")

    doc.append(NewPart)


    PersonalEntry = UnsafeCommand('newcommand', r'\PersonalEntry', options=2,
                             extra_arguments=r"""
        \noindent\hangindent=2em\hangafter=0 % Indentation
		\parbox{\spacebox}{        % Box to align text
		\textit{#1}}		       % Entry name (birth, address, etc.)
		\hspace{1.5em} #2 \par}    % Entry value
 """)

    doc.append(PersonalEntry)


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




    # Add stuff to the document
    with doc.create(Section('Experience')):
        doc.append('Some text.')


    tex = doc.dumps()  # The document as string in LaTeX syntax


    doc.generate_tex("./simple-resume")
