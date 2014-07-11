# revision 32677
# category Package
# catalog-ctan /macros/latex/contrib/easy-todo
# catalog-date 2014-01-14 11:49:17 +0100
# catalog-license apache2
# catalog-version undef
Name:		texlive-easy-todo
Version:	20140114
Release:	3
Summary:	To-do notes in a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/easy-todo
License:	APACHE2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easy-todo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easy-todo.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides to-do notes throughout a document, and
will provide an index of things to do.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/easy-todo/easy-todo.sty
%doc %{_texmfdistdir}/doc/latex/easy-todo/LICENSE
%doc %{_texmfdistdir}/doc/latex/easy-todo/README
%doc %{_texmfdistdir}/doc/latex/easy-todo/easy-todo.pdf
%doc %{_texmfdistdir}/doc/latex/easy-todo/easy-todo.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
