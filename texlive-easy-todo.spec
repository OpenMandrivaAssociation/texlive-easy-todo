Name:		texlive-easy-todo
Version:	1.0
Release:	1
Summary:	To-do notes in a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/easy-todo
License:	APACHE2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easy-todo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easy-todo.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides to-do notes throughout a document, and
will provide an index of things to do.

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
