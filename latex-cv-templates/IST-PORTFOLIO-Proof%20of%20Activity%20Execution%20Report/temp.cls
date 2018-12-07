\ProvidesClass{temp}[2016/02/01 CV]
\NeedsTeXFormat{LaTeX2e}
\DeclareOption{print}{\def\@cv@print{}}
\DeclareOption*{%
  \PassOptionsToClass{\CurrentOption}{scrartcl}
}
\ProcessOptions\relax
\LoadClass{scrartcl}

%\usepackage[english]{babel}
\usepackage[utf8x]{inputenc}
\usepackage[default,scale=0.95]{opensans}
\usepackage[T1]{fontenc}

\usepackage[protrusion=true,expansion=true]{microtype}
\usepackage{amsmath,amsfonts,amsthm}    
\usepackage[pdftex]{graphicx}
\usepackage{wrapfig}
\usepackage[hmargin=1.25cm, vmargin=0.7cm]{geometry}
\usepackage[usenames,dvipsnames]{xcolor}

\usepackage{sidecap}
\usepackage{geometry}
\usepackage{url}
\usepackage{float}

\frenchspacing              % Better looking spacings after periods
\pagestyle{empty}           % No pagenumbers/headers/footers

% Color definitions
\definecolor{date}{HTML}{666666} 
\definecolor{primary}{HTML}{191919} 
\definecolor{headings}{HTML}{025178}
\definecolor{subheadings}{HTML}{002648}


%%% Custom sectioning (sectsty package)
%%% ------------------------------------------------------------
\usepackage{sectsty}

\sectionfont{\usefont{OT1}{phv}{b}{n}\sectionrule{0pt}{0pt}{-5pt}{3pt}}
\subsectionfont{\color{headings}\usefont{OT1}{phv}{b}{n}}
\subsubsectionfont{\sectionrule{0pt}{0pt}{-5pt}{3pt}}
%%% Macros
%%% ------------------------------------------------------------
\newlength{\spacebox}
\settowidth{\spacebox}{8888888888}			% Box to align text
\newcommand{\sepspace}{\vspace*{1em}}		% Vertical space macro

\newcommand{\MyName}[1]{ % Name 
		 \huge \usefont{OT1}{phv}{b}{n} \hfill \textcolor{headings}{#1}
		\par \normalsize \normalfont}


\newcommand{\NewPart}[1]{\section*{ \color{headings} \uppercase{#1}}}

\newcommand{\PersonalEntry}[2]{
		\noindent\hangindent=2em\hangafter=0 % Indentation
		\parbox{\spacebox}{        % Box to align text
		\textit{#1}}		       % Entry name (birth, address, etc.)
		\hspace{1.5em} #2 \par}    % Entry value

\newcommand{\SkillsEntry}[2]{      % Same as \PersonalEntry
		\noindent\hangindent=2em\hangafter=0 % Indentation
		\parbox{\spacebox}{        % Box to align text
		\textit{#1}}			   % Entry name (birth, address, etc.)
		\hspace{1.5em} #2 \par}    % Entry value	
        
        
\newcommand{\workEntry}[5]{		     
    	\begin{minipage}{0.08\linewidth}
 		\includegraphics[width=1.2cm] {#5}
		\end{minipage}%                 
        \begin{minipage}{0.84\linewidth}  
    	\noindent {\color{subheadings}\bfseries\uppercase {#1}}, {\color{subheadings}\textit{#3}}  
        \hfill  {\color{headings}\fontsize{10pt}{12pt}#2}   
        \par   	
        \noindent\hangindent=2em\hangafter=0 \small #4 % Description
		\normalsize \par         
        \end{minipage}         
}
        
\newcommand{\EducationEntry}[5]{     
    	\begin{minipage}{0.08\linewidth}
 		\includegraphics[width=1.2cm] {#5}
		\end{minipage}%                    
        \begin{minipage}{0.84\linewidth}  
    	\noindent {\color{subheadings}\bfseries\uppercase {#1}} 
        \hfill {\color{headings}\fontsize{10pt}{12pt}#2}
		\par   	
		\noindent {\color{subheadings}\textit{#3}} \par 
        \noindent\hangindent=2em\hangafter=0 \small #4 % Description
		\normalsize \par         
        \end{minipage}        
 }

\newcommand{\flag}[1]{
	\includegraphics[height=9pt, width= 15pt]{#1}
}     

\newcommand{\software}[1]{
	\includegraphics[height=9pt]{#1}
}  

\newcommand{\softwareb}[1]{
	\raisebox{-.6\height}{\includegraphics[height=18pt]{#1}}
}