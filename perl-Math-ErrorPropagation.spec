#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	ErrorPropagation
Summary:	Math::ErrorPropagation - Computes the error of a function of statistical data
Summary(pl):	Math::ErrorPropagation - obliczanie b³êdu funkcji danych statystycznych
Name:		perl-Math-ErrorPropagation
Version:	0.01
Release:	2
License:	GNU/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Test-Harness
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows the propagation of errors on the variables through
various simple mathematical operations to automatically compute the
error of the function.

%description -l pl
Ten pakiet pozwala na automatycznie obliczanie b³êdu funkcji
powsta³ego z propagacji b³êdów na zmiennych poprzez ró¿ne proste
operacje matematyczne.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Math/ErrorPropagation.pm
%{_mandir}/man3/*
