# revision 30452
# category Package
# catalog-ctan /macros/latex/contrib/memory
# catalog-date 2013-05-13 20:07:16 +0200
# catalog-license lppl1.3
# catalog-version 1.2
Name:		texlive-memory
Version:	1.2
Release:	4
Summary:	Containers for data in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/memory
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/memory.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/memory.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/memory.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows the user to declare single object or array
containers.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/memory/memory.sty
%doc %{_texmfdistdir}/doc/latex/memory/README
%doc %{_texmfdistdir}/doc/latex/memory/memory.pdf
#- source
%doc %{_texmfdistdir}/source/latex/memory/memory.dtx
%doc %{_texmfdistdir}/source/latex/memory/memory.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
