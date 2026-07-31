%global octpkg io

Summary:	Input/Output in external formats
Name:		octave-io
Version:	2.7.2
Release:	1
License:	GPLv3+ and BSD
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/io/
Url:		https://packages.octave.org/io/
Source0:	https://downloads.sourceforge.net/octave/io-%{version}.tar.gz

BuildRequires:  octave-devel >= 4.2.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Input/Output in external formats.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n io-2.7.2

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

