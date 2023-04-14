Name     : kvantum
Version  : 1.0.10
Release  : 1
URL      : https://github.com/tsujan/Kvantum
Source0  : https://github.com/tsujan/Kvantum/archive/V%{version}/%{name}-%{version}.tar.gz
Summary  : A Linux SVG-based theme engine for Qt and KDE
Group    : Development/Tools
License  : GPLv3
BuildRequires : cmake
BuildRequires : mesa-dev
BuildRequires : qtbase-dev
BuildRequires : xkbcomp-dev
BuildRequires : chrpath
BuildRequires : qttools-dev kwindowsystem-dev
BuildRequires : qtbase-dev qtsvg-dev qtx11extras-dev
BuildRequires : Vulkan-Loader-dev Vulkan-Loader 
BuildRequires : Vulkan-Headers-dev Vulkan-Tools Vulkan-Headers
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

%prep
%setup -q -n Kvantum-%{version}


%build
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
cmake -B build5 -S Kvantum \
    -DCMAKE_INSTALL_PREFIX=/opt/3rd-party/bundles/clearfraction/usr 
make -C build5



%install
DESTDIR=%{buildroot} cmake --install build5 
cp -afr %{buildroot}/opt/3rd-party/bundles/clearfraction/usr %{buildroot}/
rm -rf %{buildroot}/opt
sed -i "s|LXQt|X-LXQt|" %{buildroot}/usr/share/applications/kvantummanager.desktop
sed -i "s|Exec=kvantummanager|Exec=env QT_PLUGIN_PATH=/opt/3rd-party/bundles/clearfraction/usr/lib64/qt5/plugins:/usr/lib64/qt5/plugins LD_LIBRARY_PATH=/opt/3rd-party/bundles/clearfraction/usr/lib64:\$LD_LIBRARY_PATH kvantummanager|"  %{buildroot}/usr/share/applications/kvantummanager.desktop


%files
%defattr(-,root,root,-)
/usr/bin/kvantummanager
/usr/bin/kvantumpreview
/usr/share/applications/kvantummanager.desktop
/usr/share/Kvantum
/usr/share/kvantumpreview
/usr/share/kvantummanager
/usr/share/color-schemes/
/usr/share/icons/
/usr/lib64/

# based on https://github.com/clearlinux-pkgs/qt5ct 
