# revision 15878
# category Package
# catalog-ctan /fonts/mathpazo
# catalog-date 2009-10-06 20:42:53 +0200
# catalog-license gpl
# catalog-version 1.003
Name:		texlive-mathpazo
Version:	1.003
Release:	8
Summary:	Fonts to typeset mathematics to match Palatino
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/mathpazo
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathpazo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathpazo.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathpazo.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Pazo Math fonts are a family of PostScript fonts suitable
for typesetting mathematics in combination with the Palatino
family of text fonts. The Pazo Math family is made up of five
fonts provided in Adobe Type 1 format (PazoMath, PazoMath-
Italic, PazoMath-Bold, PazoMath-BoldItalic, and
PazoMathBlackboardBold). These contain, in designs that match
Palatino, glyphs that are usually not available in Palatino and
for which Computer Modern looks odd when combined with
Palatino. These glyphs include the uppercase Greek alphabet in
upright and slanted shapes in regular and bold weights, the
lowercase Greek alphabet in slanted shape in regular and bold
weights, several mathematical glyphs (partialdiff, summation,
product, coproduct, emptyset, infinity, and proportional) in
regular and bold weights, other glyphs (Euro and dotlessj) in
upright and slanted shapes in regular and bold weights, and the
uppercase letters commonly used to represent various number
sets (C, I, N, Q, R, and Z) in blackboard bold. The set also
includes a set of 'true' small-caps fonts, also suitable for
use with Palatino (or one of its clones). LaTeX macro support
(using package mathpazo.sty) is provided in psnfss (a required
part of any LaTeX distribution).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/mathpazo/fplmb.afm
%{_texmfdistdir}/fonts/afm/public/mathpazo/fplmbb.afm
%{_texmfdistdir}/fonts/afm/public/mathpazo/fplmbi.afm
%{_texmfdistdir}/fonts/afm/public/mathpazo/fplmr.afm
%{_texmfdistdir}/fonts/afm/public/mathpazo/fplmri.afm
%{_texmfdistdir}/fonts/tfm/public/mathpazo/fplmb.tfm
%{_texmfdistdir}/fonts/tfm/public/mathpazo/fplmbb.tfm
%{_texmfdistdir}/fonts/tfm/public/mathpazo/fplmbi.tfm
%{_texmfdistdir}/fonts/tfm/public/mathpazo/fplmr.tfm
%{_texmfdistdir}/fonts/tfm/public/mathpazo/fplmri.tfm
%{_texmfdistdir}/fonts/tfm/public/mathpazo/zplmb7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathpazo/zplmb7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathpazo/zplmb7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathpazo/zplmr7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathpazo/zplmr7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathpazo/zplmr7v.tfm
%{_texmfdistdir}/fonts/tfm/public/mathpazo/zplmr7y.tfm
%{_texmfdistdir}/fonts/type1/public/mathpazo/fplmb.pfb
%{_texmfdistdir}/fonts/type1/public/mathpazo/fplmbb.pfb
%{_texmfdistdir}/fonts/type1/public/mathpazo/fplmbi.pfb
%{_texmfdistdir}/fonts/type1/public/mathpazo/fplmr.pfb
%{_texmfdistdir}/fonts/type1/public/mathpazo/fplmri.pfb
%{_texmfdistdir}/fonts/vf/public/mathpazo/zplmb7m.vf
%{_texmfdistdir}/fonts/vf/public/mathpazo/zplmb7t.vf
%{_texmfdistdir}/fonts/vf/public/mathpazo/zplmb7y.vf
%{_texmfdistdir}/fonts/vf/public/mathpazo/zplmr7m.vf
%{_texmfdistdir}/fonts/vf/public/mathpazo/zplmr7t.vf
%{_texmfdistdir}/fonts/vf/public/mathpazo/zplmr7v.vf
%{_texmfdistdir}/fonts/vf/public/mathpazo/zplmr7y.vf
%doc %{_texmfdistdir}/doc/latex/mathpazo/README.txt
%doc %{_texmfdistdir}/doc/latex/mathpazo/gpl.txt
%doc %{_texmfdistdir}/doc/latex/mathpazo/mapfplm.tex
%doc %{_texmfdistdir}/doc/latex/mathpazo/mapppl.tex
%doc %{_texmfdistdir}/doc/latex/mathpazo/mapzplm.tex
%doc %{_texmfdistdir}/doc/latex/mathpazo/pazofnst.tex
%doc %{_texmfdistdir}/doc/latex/mathpazo/pazotest.pdf
#- source
%doc %{_texmfdistdir}/source/latex/mathpazo/Makefile
%doc %{_texmfdistdir}/source/latex/mathpazo/cmbsy10.pl
%doc %{_texmfdistdir}/source/latex/mathpazo/cmbx10.pl
%doc %{_texmfdistdir}/source/latex/mathpazo/cmex10.pl
%doc %{_texmfdistdir}/source/latex/mathpazo/cmmi10.pl
%doc %{_texmfdistdir}/source/latex/mathpazo/cmmib10.pl
%doc %{_texmfdistdir}/source/latex/mathpazo/cmr10.pl
%doc %{_texmfdistdir}/source/latex/mathpazo/cmsy10.pl
%doc %{_texmfdistdir}/source/latex/mathpazo/fplmb.inf
%doc %{_texmfdistdir}/source/latex/mathpazo/fplmb.mtx
%doc %{_texmfdistdir}/source/latex/mathpazo/fplmb.pl
%doc %{_texmfdistdir}/source/latex/mathpazo/fplmbb.inf
%doc %{_texmfdistdir}/source/latex/mathpazo/fplmbb.mtx
%doc %{_texmfdistdir}/source/latex/mathpazo/fplmbb.pl
%doc %{_texmfdistdir}/source/latex/mathpazo/fplmbi.inf
%doc %{_texmfdistdir}/source/latex/mathpazo/fplmbi.mtx
%doc %{_texmfdistdir}/source/latex/mathpazo/fplmbi.pl
%doc %{_texmfdistdir}/source/latex/mathpazo/fplmr.inf
%doc %{_texmfdistdir}/source/latex/mathpazo/fplmr.mtx
%doc %{_texmfdistdir}/source/latex/mathpazo/fplmr.pl
%doc %{_texmfdistdir}/source/latex/mathpazo/fplmri.inf
%doc %{_texmfdistdir}/source/latex/mathpazo/fplmri.mtx
%doc %{_texmfdistdir}/source/latex/mathpazo/fplmri.pl
%doc %{_texmfdistdir}/source/latex/mathpazo/haxzplmb.mtx
%doc %{_texmfdistdir}/source/latex/mathpazo/haxzplmr.mtx
%doc %{_texmfdistdir}/source/latex/mathpazo/inf/fplmb.inf
%doc %{_texmfdistdir}/source/latex/mathpazo/inf/fplmbb.inf
%doc %{_texmfdistdir}/source/latex/mathpazo/inf/fplmbi.inf
%doc %{_texmfdistdir}/source/latex/mathpazo/inf/fplmr.inf
%doc %{_texmfdistdir}/source/latex/mathpazo/inf/fplmri.inf
%doc %{_texmfdistdir}/source/latex/mathpazo/nokernum.mtx
%doc %{_texmfdistdir}/source/latex/mathpazo/omsnames.mtx
%doc %{_texmfdistdir}/source/latex/mathpazo/pazofnst/Makefile
%doc %{_texmfdistdir}/source/latex/mathpazo/pazofnst/cmbsy10.pl
%doc %{_texmfdistdir}/source/latex/mathpazo/pazofnst/cmbx10.pl
%doc %{_texmfdistdir}/source/latex/mathpazo/pazofnst/cmex10.pl
%doc %{_texmfdistdir}/source/latex/mathpazo/pazofnst/cmmi10.pl
%doc %{_texmfdistdir}/source/latex/mathpazo/pazofnst/cmmib10.pl
%doc %{_texmfdistdir}/source/latex/mathpazo/pazofnst/cmr10.pl
%doc %{_texmfdistdir}/source/latex/mathpazo/pazofnst/cmsy10.pl
%doc %{_texmfdistdir}/source/latex/mathpazo/pazofnst/haxzplmb.mtx
%doc %{_texmfdistdir}/source/latex/mathpazo/pazofnst/haxzplmr.mtx
%doc %{_texmfdistdir}/source/latex/mathpazo/pazofnst/nokernum.mtx
%doc %{_texmfdistdir}/source/latex/mathpazo/pazofnst/omsnames.mtx
%doc %{_texmfdistdir}/source/latex/mathpazo/pazofnst/pazofnst.tex
%doc %{_texmfdistdir}/source/latex/mathpazo/pazofnst/unsetcm4pl.mtx
%doc %{_texmfdistdir}/source/latex/mathpazo/pazofnst/unsetint.mtx
%doc %{_texmfdistdir}/source/latex/mathpazo/pazofnst/unsetosf.mtx
%doc %{_texmfdistdir}/source/latex/mathpazo/pazofnst/unsetpl4cm.mtx
%doc %{_texmfdistdir}/source/latex/mathpazo/pazofnst/unsetpunct.mtx
%doc %{_texmfdistdir}/source/latex/mathpazo/pazofnst/zplmbgop.mtx
%doc %{_texmfdistdir}/source/latex/mathpazo/pazofnst/zplmsum.mtx
%doc %{_texmfdistdir}/source/latex/mathpazo/pplr8a.mtx
%doc %{_texmfdistdir}/source/latex/mathpazo/unsetcm4pl.mtx
%doc %{_texmfdistdir}/source/latex/mathpazo/unsetint.mtx
%doc %{_texmfdistdir}/source/latex/mathpazo/unsetosf.mtx
%doc %{_texmfdistdir}/source/latex/mathpazo/unsetpl4cm.mtx
%doc %{_texmfdistdir}/source/latex/mathpazo/unsetpunct.mtx
%doc %{_texmfdistdir}/source/latex/mathpazo/zplmbgop.mtx
%doc %{_texmfdistdir}/source/latex/mathpazo/zplmsum.mtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.003-2
+ Revision: 753779
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.003-1
+ Revision: 718974
- texlive-mathpazo
- texlive-mathpazo
- texlive-mathpazo
- texlive-mathpazo

