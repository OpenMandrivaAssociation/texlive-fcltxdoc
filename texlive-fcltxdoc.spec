# revision 24500
# category Package
# catalog-ctan /macros/latex/contrib/fcltxdoc
# catalog-date 2011-11-03 08:30:49 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-fcltxdoc
Version:	1.0
Release:	7
Summary:	Macros for use in the author's documentation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fcltxdoc
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fcltxdoc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fcltxdoc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fcltxdoc.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is not advertised for public use, but is necessary
for the support of others of the author's packages (which are
compiled under the ltxdoc class).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fcltxdoc/fcltxdoc.sty
%doc %{_texmfdistdir}/doc/latex/fcltxdoc/fcltxdoc.pdf
#- source
%doc %{_texmfdistdir}/source/latex/fcltxdoc/fcltxdoc.drv
%doc %{_texmfdistdir}/source/latex/fcltxdoc/fcltxdoc.dtx
%doc %{_texmfdistdir}/source/latex/fcltxdoc/fcltxdoc.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 751797
- Rebuild to reduce used resources

* Thu Nov 10 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 729658
- texlive-fcltxdoc
- texlive-fcltxdoc

