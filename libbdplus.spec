Name:           libbdplus
Version:        0.1.0
Release:        4%{?dist}
Summary:        Open implementation of BD+ protocol
License:        LGPLv2+
URL:            http://www.videolan.org/developers/libbdplus.html
Source0:        ftp://ftp.videolan.org/pub/videolan/%{name}/%{version}/%{name}-%{version}.tar.bz2
# http://git.videolan.org/gitweb.cgi/libbdplus.git/?p=libbdplus.git;a=patch;h=a47d4a95762d960653599d83281d4ede92663b99
Patch0:         libbdplus-0.1.0-libgcrypt_1.6_support.patch

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
%patch0 -p1 -b .libgcrypt-1.6


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
* Sat Apr 26 2014 Xavier Bachelot <xavier@bachelot.org> - 0.1.0-4
- Add patch for libgcrypt 1.6 support.

* Sat Apr 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.1.0-3
- Rebuilt for libgcrypt

* Wed Jan 08 2014 Xavier Bachelot <xavier@bachelot.org> 0.1.0-2
- Add version to libaacs BuildRequires:.
- Remove Group: tags.
- Use %%make_install macro.
- Minor specfile fixes.

* Fri Dec 27 2013 Xavier Bachelot <xavier@bachelot.org> 0.1.0-1
- Initial release.
