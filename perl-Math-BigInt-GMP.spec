%define upstream_name    Math-BigInt-GMP
%define upstream_version 1.36

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	High speed arbitrary size integer math
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Math/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	gmp-devel
BuildRequires:	perl(YAML)
# automatic dependency doesn't work here, because perl package
# provides an unversioned one
BuildRequires:	perl-Math-BigInt >= 1.87
BuildRequires:	perl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
This package contains a replacement (drop-in) module for
Math::BigInt's core, Math::BigInt::Calc.pm.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
export PERL5LIB=%{perl_vendorlib}
perl Makefile.PL INSTALLDIRS="vendor"
%make  CFLAGS="%{optflags}"

%check
export PERL5LIB=%{perl_vendorlib}
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc build BUGS CHANGES CREDITS INSTALL LICENSE README SIGNATURE TODO
%{perl_vendorarch}/Math
%{perl_vendorarch}/auto/Math
%{_mandir}/man*/*
