#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	ErrorPropagation
Summary:	Math::ErrorPropagation - computes the error of a function of statistical data
Summary(pl.UTF-8):   Math::ErrorPropagation - obliczanie błędu funkcji danych statystycznych
Name:		perl-Math-ErrorPropagation
Version:	0.01
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	089bc0978360afc1e9ba94767975cb8f
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
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

%description -l pl.UTF-8
Ten pakiet pozwala na automatycznie obliczanie błędu funkcji
powstałego z propagacji błędów na zmiennych poprzez różne proste
operacje matematyczne.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

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
