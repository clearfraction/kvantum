Name     : kvantum
Version  : 1.0.9
Release  : 1
URL      : https://github.com/tsujan/Kvantum/
Source0  : https://github.com/tsujan/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Summary  : A Linux SVG-based theme engine for Qt and KDE
Group    : Development/Tools
License  : GPLv3
BuildRequires : cmake
BuildRequires : mesa-dev
BuildRequires : qtbase-dev
BuildRequires : xkbcomp-dev
BuildRequires : chrpath
BuildRequires : qttools-dev
BuildRequires : qtbase-dev
BuildRequires:  Vulkan-Loader-dev Vulkan-Loader 
BuildRequires:  Vulkan-Headers-dev Vulkan-Tools Vulkan-Headers
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-cursor)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xinerama)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : pkgconfig(xrandr)
BuildRequires : pkgconfig(xscrnsaver)
BuildRequires : pkgconfig(xpresent)
BuildRequires : pkgconfig(xv)


%description
Kvantum is an SVG-based theme engine for Qt5, KDE and LXQt, with an emphasis
on elegance, usability and practicality.


%setup -q -n Kvantum-%{version}
cd %{_builddir}/Kvantum-%{version}

%build
export LANG=C.UTF-8
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
rm -rf %{buildroot}
pushd clr-build
%make_install
sed -i "s|LXQt|X-LXQt|" %{buildroot}/usr/share/applications/kvantummanager.desktop
popd

%files
%defattr(-,root,root,-)
/usr/bin/kvantummanager
/usr/bin/kvantumpreview
/usr/share/applications/qt6ct.desktop
/usr/share/Kvantum/
/usr/share/kvantumpreview
/usr/share/kvantummanager
/usr/share/themes/Kv*/
/usr/lib64/

# based on https://github.com/clearlinux-pkgs/qt5ct 
