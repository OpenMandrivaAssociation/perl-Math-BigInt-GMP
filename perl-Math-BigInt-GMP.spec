%define	modname	Math-BigInt-GMP
%define modver 1.38

Summary:	High speed arbitrary size integer math

Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Math/%{modname}-%{modver}.tar.gz
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test)
BuildRequires:	gmp-devel
BuildRequires:	perl(YAML)
# automatic dependency doesn't work here, because perl package
# provides an unversioned one
BuildRequires:	perl-Math-BigInt >= 1.87
BuildRequires:	perl-devel

%description
This package contains a replacement (drop-in) module for
Math::BigInt's core, Math::BigInt::Calc.pm.

%prep
%autosetup -p1 -n %{modname}-%{modver}

%build
export PERL5LIB=%{perl_vendorlib}
perl Makefile.PL INSTALLDIRS="vendor"
%make_build CFLAGS="%{optflags}"

%install
%make_install

%files
%doc build BUGS CHANGES CREDITS INSTALL LICENSE README SIGNATURE TODO
%{perl_vendorarch}/Math
%{perl_vendorarch}/auto/Math
%doc %{_mandir}/man3/*
