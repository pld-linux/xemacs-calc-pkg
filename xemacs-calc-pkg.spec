Summary:	[X]Emacs calculator
Summary(pl):	Kalkulator dla [X]Emacsa
Name:		xemacs-calc-pkg
%define 	srcname	calc
Version:	1.18
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Group(cs):	Aplikace/Editory/Emacs
Group(da):	Programmer/Tekstbehandlere/Emacs
Group(de):	Applikationen/Editoren/Emacs
Group(es):	Aplicaciones/Editores/Emacs
Group(fr):	Applications/Editeurs/Emacs
Group(is):	Forrit/Ritlar/Emacs
Group(it):	Applicazioni/Editor/Emacs
Group(ja):	•¢•◊•Í•±°º•∑•Á•Û/•®•«•£•ø/Emacs
Group(no):	Applikasjoner/Editorer/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Group(pt):	AplicaÁıes/Editores/Emacs
Group(ru):	“…Ãœ÷≈Œ…—/Ú≈ƒ¡À‘œ“Ÿ/Emacs
Group(sl):	Programi/Urejevalniki/Emacs
Group(sv):	Till‰mpningar/Editorer/Emacs
Group(uk):	“…ÀÃ¡ƒŒ¶ “œ«“¡Õ…/Ú≈ƒ¡À‘œ“…/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
#Patch0:	xemacs-calc-pkg-info.patch
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scientific, financial, and symbolic calculator for [X]Emacs.

%description -l pl 
Naukowy, finansowy i symboliczny kalkulator dla [X]Emacsa.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

gzip -9nf lisp/calc/ChangeLog 

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/xemacs-packages%{_sysconfdir}/*
%doc lisp/calc/ChangeLog.gz 
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.elc
