import json
from pylatex.base_classes import Environment, CommandBase, Arguments
from pylatex.package import Package
from pylatex import Document, Section, Subsection, Command, UnsafeCommand
from pylatex.utils import NoEscape, italic


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

class PublicationsEntry(CommandBase):
    _latex_name = "PublicationsEntry"

class CertificationsEntry(CommandBase):
    _latex_name = "CertificationsEntry"



#######################################





if __name__ == '__main__':


    doc = Document(documentclass = 'scrartcl' , document_options = ["paper=a4","fontsize=11pt"])


###########################

###########################



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


    doc.append(Command('frenchspacing'))
    doc.append(Command('pagestyle', 'empty'))
    doc.append(Command("textheight=700px"))
    doc.append(Command("sectionfont", NoEscape(r""" \usefont{OT1}{phv}{b}{n} \sectionrule{0pt}{0pt}{-5pt}{3pt}}""")))
    doc.append(Command("newlength",Command("spacebox")))
    doc.append(Command("settowidth",[Command("spacebox"), "8888888888"]))

###########################

###########################

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


###########################

###########################



    MySlogan = UnsafeCommand('newcommand', r'\MySlogan', options=1,
                             extra_arguments=r"""
        \large \usefont{OT1}{phv}{m}{n}\hfill \textit{#1}
        \par \normalsize \normalfont
""")


    doc.append(MySlogan)


###########################

###########################



    NewPart = UnsafeCommand('newcommand', r'\NewPart', options=1,
                             extra_arguments=r"""
                             \section*{\uppercase{#1}}
""")

    doc.append(NewPart)


###########################

###########################



    PersonalEntry = UnsafeCommand('newcommand', r'\PersonalEntry', options=2,
                             extra_arguments=r"""
        \noindent\hangindent=2em\hangafter=0 % Indentation
        \parbox{\spacebox}{        % Box to align text
        \textit{#1}}               % Entry name (birth, address, etc.)
        \hspace{1.5em} #2 \par}    % Entry value
 """)

    doc.append(PersonalEntry)


###########################

###########################



    SkillsEntry = UnsafeCommand('newcommand', r'\SkillsEntry', options=2,
                             extra_arguments=r"""

        \noindent\hangindent=2em\hangafter=0 % Indentation
        \parbox{\spacebox}{        % Box to align text
        \textit{#1}}			   % Entry name (birth, address, etc.)
        \hspace{1.5em} #2 \par    % Entry value
""")

    doc.append(SkillsEntry)

###########################

###########################



    EducationEntry = UnsafeCommand('newcommand', r'\EducationEntry', options=4,
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


###########################

###########################



    WorkEntry = UnsafeCommand('newcommand', r'\WorkEntry', options=4,
                             extra_arguments=r"""
         % Same as \EducationEntry
        \noindent \textbf{#1} \hfill      % Jobname
        \colorbox{Black}{\color{White}#2} \par  % Duration
        \noindent \textit{#3} \par              % Company
        \noindent\hangindent=2em\hangafter=0 \small #4 % Description
        \normalsize \par
 """)

    doc.append(WorkEntry)


###########################

###########################



    PublicationsEntry = UnsafeCommand('newcommand', r'\PublicationsEntry', options=5,
                             extra_arguments=r"""
         % Same as \EducationEntry
        \noindent \textbf{#1} \hfill      % Jobname
        \colorbox{Black}{\color{White}#2} \par  % Duration
        \noindent \textit{#3} \par              % Company
        \noindent\hangindent=2em\hangafter=0 \small #4 \par % Publisher
        \noindent\hangindent=2em\hangafter=0 \small #5 % Description
        \normalsize \par
 """)

    doc.append(PublicationsEntry)


###########################

###########################

#     CertificationsEntry = UnsafeCommand('newcommand', r'\CertificationsEntry', options=2,
#                              extra_arguments=r"""

#          % Same as \EducationEntry
#         \noindent \textbf{#1} \hfill      % Jobname
#         \noindent \textit{#2} \par              % Company
#         \normalsize \par

# """)



    CertificationsEntry = UnsafeCommand('newcommand', r'\CertificationsEntry', options=3,
                             extra_arguments=r"""

         % Same as \EducationEntry
        \noindent \textbf{#1} \hfill      % Certification Name
        \colorbox{Black}{\color{White}#2} \par  % Duration
        \noindent \textit{#3} \par              % University
%        \noindent\hangindent=2em\hangafter=0 \small #4 % Description
        \normalsize \par

""")



    doc.append(CertificationsEntry)

###########################
# Personal Details
###########################



# TODO photograph
# %\begin{wrapfigure}{l}{0.5\textwidth}
# %	\vspace*{-2em}
# %		\includegraphics[width=0.15\textwidth]{photo}
# %\end{wrapfigure}

    doc.append(Command("MyName","Abhinav Sharma"))

    doc.append(Command('MySlogan', 'Curriculum Vitae'))

    doc.append(Command('sepspace'))

    doc.append(Command('NewPart', ["Personal details", NoEscape("")]))

    doc.append(Command('PersonalEntry', ["Birth", "March 29, 1993"]))

    doc.append(Command('PersonalEntry' , ["Address",
                                          NoEscape("458, Pocket-1, DDA SFS Flats, Sector-9, Dwarka, N.D. - 110077")]))

    doc.append(Command('PersonalEntry', ["Phone", "(+91) 9650691024"]))
#TODO url
   # doc.append(Command('PersonalEntry'["Mail", "\url{me@home.com}"]))

###########################
# Education Details
###########################



    doc.append(Command('NewPart', ["Education details", NoEscape("")]))


    doc.append(Command('sepspace'))

    doc.append(Command("EducationEntry", [ "B.Tech (Computer Science Department, specialization in IT)",
                                       NoEscape("2012-2016"),
                                       "Delhi Technological University (formerly Delhi College of Engineering)",
                                       """I secured an All India Rank of 9000 out of 1.2 million students and cleared the cut-off for the prestigious Computer Science department. In addition to the Degree curicullum, I read and reviewed about 200 books on  - Literature - Philosophy - Fiction  All the reviews can be read on my Goodreads.com profile https://www.goodreads.com/user/show/10604145-harsh-sharma"""]))



#Institute of Engineering and Technology,2011,2012,"Secured a State Rank of 1378 and thus a General Category seat in Computer Science department.  I studied in IET for the duration of one year, prepared again for the Delhi College of Engineering ( DTU ) and when I got selected in DTU - I withdrew my admission.",Bachelor's degree,


###########################
# Skills Details
###########################



    doc.append(Command('NewPart', ["Skills", NoEscape("")]))

    doc.append(Command("SkillsEntry", [ "Human Languages", "English"]))

    doc.append(Command("SkillsEntry", [ NoEscape(""), "Hindi"]))

    doc.append(Command("SkillsEntry", [ NoEscape(""), "Portuguese"]))

    doc.append(Command("SkillsEntry", [ NoEscape(""), "Russian"]))

    doc.append(Command("SkillsEntry", [ NoEscape(""), "German"]))

#    doc.append(Command("SkillsEntry", [ NoEscape(""), "Korean"]))

    doc.append(Command('sepspace'))

    doc.append(Command("SkillsEntry", [ "Programming Languages", "Clojure ( JVM )"]))

    doc.append(Command("SkillsEntry", [NoEscape("") , "ClojureScript (NodeJS)"]))

    doc.append(Command("SkillsEntry", [NoEscape("") , "OCaml"]))

    doc.append(Command("SkillsEntry", [NoEscape("") , "Go"]))

    doc.append(Command("SkillsEntry", [NoEscape("") , "C"]))

    doc.append(Command("SkillsEntry", [NoEscape("") , "Python"]))

    doc.append(Command("SkillsEntry", [NoEscape("") , "Julia"]))

    doc.append(Command("SkillsEntry", [NoEscape("") , "PowerShell"]))




###########################
# Work Details
###########################


    doc.append(Command('NewPart', ["Work details", NoEscape("")]))

    doc.append(Command("WorkEntry",["Chief Technology Officer and Product Strategist", NoEscape("August 2018 - Present"), "Cyber Indian App Stores", """I am leading a team of 8 in the core engineering wing."""]))

    doc.append(Command('sepspace'))

    doc.append(Command("WorkEntry",["Machine Learning Engineer and Product Strategist", NoEscape("1 January 2018 - 1 August 2018"), "Cyber Indian App Stores", """Working on, devnagri.com focusing on the application of Machine Learning and Natural Language Processing techniques in service of Indian languages."""]))

    doc.append(Command('sepspace'))

    doc.append(Command("WorkEntry",[NoEscape("Software Engineer - Machine Learning"), NoEscape("August 2016 - July 2017"), "Fourtek (IT) Solutions Pvt. Ltd.", """I worked as a co-founder of a product targeting the StartUp ecosystem."""]))

    doc.append(Command('sepspace'))

    doc.append(Command("WorkEntry",[NoEscape("Creative Writer"), NoEscape("1 July 2017 - Present"), "Medium.com", """My creative Scribblings can be viewed at my Medium.com blog."""]))

    doc.append(Command('sepspace'))

    doc.append(Command("WorkEntry",[NoEscape("Community Mentor"), NoEscape("1 April 2017 - Present"), "Coursera.com", """I was invited to become a member of the Coursear Mentorship program in which I had to guide individual learners in their online learning journey."""]))

    doc.append(Command('sepspace'))

    doc.append(Command("WorkEntry",[NoEscape("Student"), NoEscape("1 August 2016 - 1 August 2017"), "Coursera.com", """I took a sabbatical following my stint with Peoplemetrix Pvt. Ltd. and I was laser focused on gaining knowledge.  This resulted in scholarships and certifications which are enlisted in the achievements section."""]))

    doc.append(Command('sepspace'))

    doc.append(Command("WorkEntry",[NoEscape("Co-Founder and Chief Technology Officer"), NoEscape("1 August 2015 - 1 July 2016"), "Coursera.com", NoEscape("""I worked on our own product targeting the  StartUps' Funding problem, under the tutelage of Fourtek IT Solutions  Pvt. Ltd. Noida, India. I withdrew from the venture realizing that there is much that I have to learn and this huge responsibility would cripple my agility.""")]))



###########################
# Publication Details
###########################

    doc.append(Command('NewPart', ["Publication details", NoEscape("")]))


    doc.append(Command("PublicationsEntry",
                       [NoEscape("An Analytical Study to Find the Major Factors Behind the Great Smog of Delhi, 2016: Using Fundamental Data Sciences"),
                        NoEscape("Mar 8, 2018"),
                        "Springer",
                        """Guided two undergraduates into the art of storytelling through Data and their hard work eventually landed a paper in the Springer publications."""]))

    doc.append(Command('sepspace'))

    doc.append(Command("PublicationsEntry",
                       [NoEscape("An Analytical Study to Find the Major Factors Behind the Great Smog of Delhi, 2016: Using Fundamental Data Sciences"),
                        NoEscape("Mar 8, 2018"),
                        "Springer",
                        """Guided two undergraduates into the art of storytelling through Data and their hard work eventually landed a paper in the Springer publications."""]))

    doc.append(Command('sepspace'))

###########################
# Certifications
###########################


    doc.append(Command('NewPart', ["Certifications", NoEscape("")]))

    with open('./Certifications.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())


    for i in range(len(data)):
        #print(i)
        doc.append(Command("CertificationsEntry",
                       [NoEscape(data[i]['Name']),
                        NoEscape(data[i]['Start Date']),
                        NoEscape(data[i]['Authority'])]))
        doc.append(Command('sepspace'))

###########################
# Generate the TEX document
###########################



    tex = doc.dumps()  # The document as string in LaTeX syntax

    doc.generate_tex("./abhi18av")
