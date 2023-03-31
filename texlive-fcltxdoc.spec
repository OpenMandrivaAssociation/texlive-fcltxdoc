Name:		texlive-fcltxdoc
Version:	24500
Release:	2
Summary:	Macros for use in the author's documentation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fcltxdoc
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fcltxdoc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fcltxdoc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fcltxdoc.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
