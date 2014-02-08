# revision 21157
# category Package
# catalog-ctan /macros/latex/contrib/easy-todo
# catalog-date 2011-01-20 10:27:03 +0100
# catalog-license apache2
# catalog-version 1.0
Name:		texlive-easy-todo
Version:	1.0
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 751282
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718294
- texlive-easy-todo
- texlive-easy-todo
- texlive-easy-todo
- texlive-easy-todo

