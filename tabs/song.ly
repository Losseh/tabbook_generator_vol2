\section{Song - example}
An easy song to learn on the piano is Mary Had a Little Lamb:\\
\begin{lilypond}
    \score { % start of musical score
      <<
        % beginning of musical staff. the \relative c' means that the
        % notes are an octave higher than the default (ie: notes are
        % notes are relative to middle c)
        \new Staff \relative c' {
            e4 d c d e e e2 d4 d d2 e4 g g2
            e4 d c d e e e e d d e d c1
        } % end of staff
      >>
    } % end of musical score
\end{lilypond}
