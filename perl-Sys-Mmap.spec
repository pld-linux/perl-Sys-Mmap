#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Sys
%define		pnam	Mmap
Summary:	Sys::Mmap - Perl module that allows to use mmap to map in a file as a Perl variable
Name:		perl-Sys-Mmap
Version:	0.21
Release:	1
# sae as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://cpan.metacpan.org/authors/id/T/TO/TODDR/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	54b46bc153c3fd36dba79b7bab2502d8
URL:		http://search.cpan.org/dist/Sys-Mmap/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mmap - uses mmap to map in a file as a Perl variable.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_vendorarch}/Sys/*.pm
%dir %{perl_vendorarch}/auto/Sys/Mmap
%attr(755,root,root) %{perl_vendorarch}/auto/Sys/Mmap/*.so
%{_mandir}/man3/*
