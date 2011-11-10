# revision 24500
# category Package
# catalog-ctan /macros/latex/contrib/fcltxdoc
# catalog-date 2011-11-03 08:30:49 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-fcltxdoc
Version:	1.0
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package is not advertised for public use, but is necessary
for the support of others of the author's packages (which are
compiled under the ltxdoc class).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fcltxdoc/fcltxdoc.sty
%doc %{_texmfdistdir}/doc/latex/fcltxdoc/fcltxdoc.pdf
#- source
%doc %{_texmfdistdir}/source/latex/fcltxdoc/fcltxdoc.drv
%doc %{_texmfdistdir}/source/latex/fcltxdoc/fcltxdoc.dtx
%doc %{_texmfdistdir}/source/latex/fcltxdoc/fcltxdoc.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
