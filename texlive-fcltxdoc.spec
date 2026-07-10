%global tl_name fcltxdoc
%global tl_revision 24500

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Macros for use in the authors documentation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fcltxdoc
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fcltxdoc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fcltxdoc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fcltxdoc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is not advertised for public use, but is necessary for the
support of others of the author's packages (which are compiled under the
ltxdoc class).

