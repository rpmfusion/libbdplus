Name:           libbdplus
Version:        0.1.0
Release:        2%{?dist}
Summary:        Open implementation of BD+ protocol
License:        LGPLv2+
URL:            http://www.videolan.org/developers/libbdplus.html
Source0:        ftp://ftp.videolan.org/pub/videolan/%{name}/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  libgcrypt-devel
BuildRequires:  libaacs-devel >= 0.7.0


%description
libbdplus is a research project to implement the BD+ System Specifications.
This research project provides, through an open-source library, a way to
understand how the BD+ protocol works.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
%make_install
find %{buildroot} -name '*.la' -delete


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc COPYING ChangeLog README.txt
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Wed Jan 08 2014 Xavier Bachelot <xavier@bachelot.org> 0.1.0-2
- Add version to libaacs BuildRequires:.
- Remove Group: tags.
- Use %%make_install macro.
- Minor specfile fixes.

* Fri Dec 27 2013 Xavier Bachelot <xavier@bachelot.org> 0.1.0-1
- Initial release.
