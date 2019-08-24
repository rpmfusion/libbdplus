Name:           libbdplus
Version:        0.1.2
Release:        8%{?dist}
Summary:        Open implementation of BD+ protocol
License:        LGPLv2+
URL:            http://www.videolan.org/developers/libbdplus.html
Source0:        ftp://ftp.videolan.org/pub/videolan/%{name}/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
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
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -delete


%ldconfig_scriptlets


%files
%doc ChangeLog README.txt
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 20 2018 Xavier Bachelot <xavier@bachelot.org> - 0.1.2-5
- Add BR: gcc.
- Use %%license.
- Use %%ldconfig_scriptlets.

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 27 2015 Xavier Bachelot <xavier@bachelot.org> - 0.1.2-1
- Update to 0.1.2.

* Mon Sep 01 2014 Sérgio Basto <sergio@serjux.com> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 04 2014 Xavier Bachelot <xavier@bachelot.org> - 0.1.1-1
- Update to 0.1.1.

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
