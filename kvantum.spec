Name     : kvantum
Version  : 1.0.10
Release  : 1
URL      : https://github.com/tsujan/Kvantum
Source0  : https://github.com/tsujan/Kvantum/archive/V%{version}/%{name}-%{version}.tar.gz
Summary  : A Linux SVG-based theme engine for Qt and KDE
Group    : Development/Tools
License  : GPLv3
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : mesa-dev
BuildRequires : qt6base-dev
BuildRequires : qt6svg-dev qt6tools-dev
BuildRequires : qtbase-dev 
BuildRequires : qttools-dev kwindowsystem-dev
BuildRequires : qtsvg-dev qtx11extras-dev
BuildRequires : xkbcomp-dev
BuildRequires : Vulkan-Loader-dev 
BuildRequires : Vulkan-Headers-dev
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
# sed -e 's|Qt6 Qt5|Qt6|' -i Kvantum/*/CMakeLists.txt


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

cmake -B build6 -S Kvantum \
    -DCMAKE_INSTALL_PREFIX=/opt/3rd-party/bundles/clearfraction/usr \
    -DENABLE_QT5=OFF -DQT_DEBUG_FIND_PACKAGE=ON
make -C build6

%install
DESTDIR=%{buildroot} cmake --install build5 
cp -afr %{buildroot}/opt/3rd-party/bundles/clearfraction/usr %{buildroot}/
rm -rf %{buildroot}/opt
# doesn't works DESTDIR=%%{buildroot} cmake --install build6
install -Dm644 build6/style/libkvantum.so %{buildroot}/usr/lib64/qt6/plugins/styles/libkvantum.so
sed -i "s|LXQt|X-LXQt|" %{buildroot}/usr/share/applications/kvantummanager.desktop
sed -i "s|Exec=kvantummanager|Exec=env QT_PLUGIN_PATH=/opt/3rd-party/bundles/clearfraction/usr/lib64/qt5/plugins:/opt/3rd-party/bundles/clearfraction/usr/lib64/qt6/plugins:/usr/lib64/qt5/plugins LD_LIBRARY_PATH=/opt/3rd-party/bundles/clearfraction/usr/lib64/:\$LD_LIBRARY_PATH kvantummanager|"  %{buildroot}/usr/share/applications/kvantummanager.desktop


%files
%defattr(-,root,root,-)
/usr/bin/kvantummanager
/usr/bin/kvantumpreview
/usr/share/applications/kvantummanager.desktop
/usr/share/Kvantum/
/usr/share/kvantumpreview
/usr/share/kvantummanager
/usr/share/color-schemes/
/usr/share/icons/
/usr/lib64/

# based on https://github.com/clearlinux-pkgs/qt5ct
