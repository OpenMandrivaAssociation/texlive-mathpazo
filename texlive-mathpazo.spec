%global tl_name mathpazo
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.003
Release:	%{tl_revision}.1
Summary:	Fonts to typeset mathematics to match Palatino
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/mathpazo
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathpazo.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathpazo.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathpazo.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(fpl)
Requires:	texlive(palatino)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The Pazo Math fonts are a family of PostScript fonts suitable for
typesetting mathematics in combination with the Palatino family of text
fonts. The Pazo Math family is made up of five fonts provided in Adobe
Type 1 format (PazoMath, PazoMath-Italic, PazoMath-Bold, PazoMath-
BoldItalic, and PazoMathBlackboardBold). These contain, in designs that
match Palatino, glyphs that are usually not available in Palatino and
for which Computer Modern looks odd when combined with Palatino. These
glyphs include the uppercase Greek alphabet in upright and slanted
shapes in regular and bold weights, the lowercase Greek alphabet in
slanted shape in regular and bold weights, several mathematical glyphs
(partialdiff, summation, product, coproduct, emptyset, infinity, and
proportional) in regular and bold weights, other glyphs (Euro and
dotlessj) in upright and slanted shapes in regular and bold weights, and
the uppercase letters commonly used to represent various number sets (C,
I, N, Q, R, and Z) in blackboard bold. LaTeX macro support (using
package mathpazo.sty) is provided in psnfss (a required part of any
LaTeX distribution).

