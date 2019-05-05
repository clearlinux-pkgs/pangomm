#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pangomm
Version  : 2.42.0
Release  : 8
URL      : https://download.gnome.org/sources/pangomm/2.42/pangomm-2.42.0.tar.xz
Source0  : https://download.gnome.org/sources/pangomm/2.42/pangomm-2.42.0.tar.xz
Summary  : C++ bindings for Pango
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: pangomm-data = %{version}-%{release}
Requires: pangomm-lib = %{version}-%{release}
Requires: pangomm-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : pkgconfig(cairomm-1.0)
BuildRequires : pkgconfig(glibmm-2.4)
BuildRequires : pkgconfig(pangocairo)

%description
Building gtkmm on Win32
===========================
Currently, both the mingw (native win32) gcc compiler and MS Visual
Studio 2013 are supported. gtkmm can be built with mingw32-gcc using
the gnu autotools (automake, autoconf, libtool). As explicitly
stated in the gtk+ for win32 distribution (http://www.gimp.org/win32/),
the gcc compiler provided by the cygwin distribution should not be
used to build gtk+/gtkmm libraries and/or applications (see the
conflicts between the cygwin and msvcrt runtime environments.

%package data
Summary: data components for the pangomm package.
Group: Data

%description data
data components for the pangomm package.


%package dev
Summary: dev components for the pangomm package.
Group: Development
Requires: pangomm-lib = %{version}-%{release}
Requires: pangomm-data = %{version}-%{release}
Provides: pangomm-devel = %{version}-%{release}
Requires: pangomm = %{version}-%{release}

%description dev
dev components for the pangomm package.


%package doc
Summary: doc components for the pangomm package.
Group: Documentation

%description doc
doc components for the pangomm package.


%package lib
Summary: lib components for the pangomm package.
Group: Libraries
Requires: pangomm-data = %{version}-%{release}
Requires: pangomm-license = %{version}-%{release}

%description lib
lib components for the pangomm package.


%package license
Summary: license components for the pangomm package.
Group: Default

%description license
license components for the pangomm package.


%prep
%setup -q -n pangomm-2.42.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557022190
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1557022190
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pangomm
cp COPYING %{buildroot}/usr/share/package-licenses/pangomm/COPYING
cp COPYING.tools %{buildroot}/usr/share/package-licenses/pangomm/COPYING.tools
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/pangomm-1.4/proc/m4/convert.m4
/usr/lib64/pangomm-1.4/proc/m4/convert_pango.m4
/usr/lib64/pangomm-1.4/proc/m4/convert_pangomm.m4

%files data
%defattr(-,root,root,-)
/usr/share/devhelp/books/pangomm-1.4/pangomm-1.4.devhelp2

%files dev
%defattr(-,root,root,-)
/usr/include/pangomm-1.4/pangomm.h
/usr/include/pangomm-1.4/pangomm/attributes.h
/usr/include/pangomm-1.4/pangomm/attriter.h
/usr/include/pangomm-1.4/pangomm/attrlist.h
/usr/include/pangomm-1.4/pangomm/cairofontmap.h
/usr/include/pangomm-1.4/pangomm/color.h
/usr/include/pangomm-1.4/pangomm/context.h
/usr/include/pangomm-1.4/pangomm/coverage.h
/usr/include/pangomm-1.4/pangomm/font.h
/usr/include/pangomm-1.4/pangomm/fontdescription.h
/usr/include/pangomm-1.4/pangomm/fontface.h
/usr/include/pangomm-1.4/pangomm/fontfamily.h
/usr/include/pangomm-1.4/pangomm/fontmap.h
/usr/include/pangomm-1.4/pangomm/fontmetrics.h
/usr/include/pangomm-1.4/pangomm/fontset.h
/usr/include/pangomm-1.4/pangomm/glyph.h
/usr/include/pangomm-1.4/pangomm/glyphstring.h
/usr/include/pangomm-1.4/pangomm/init.h
/usr/include/pangomm-1.4/pangomm/item.h
/usr/include/pangomm-1.4/pangomm/language.h
/usr/include/pangomm-1.4/pangomm/layout.h
/usr/include/pangomm-1.4/pangomm/layoutiter.h
/usr/include/pangomm-1.4/pangomm/layoutline.h
/usr/include/pangomm-1.4/pangomm/layoutrun.h
/usr/include/pangomm-1.4/pangomm/private/attributes_p.h
/usr/include/pangomm-1.4/pangomm/private/attriter_p.h
/usr/include/pangomm-1.4/pangomm/private/attrlist_p.h
/usr/include/pangomm-1.4/pangomm/private/cairofontmap_p.h
/usr/include/pangomm-1.4/pangomm/private/color_p.h
/usr/include/pangomm-1.4/pangomm/private/context_p.h
/usr/include/pangomm-1.4/pangomm/private/coverage_p.h
/usr/include/pangomm-1.4/pangomm/private/font_p.h
/usr/include/pangomm-1.4/pangomm/private/fontdescription_p.h
/usr/include/pangomm-1.4/pangomm/private/fontface_p.h
/usr/include/pangomm-1.4/pangomm/private/fontfamily_p.h
/usr/include/pangomm-1.4/pangomm/private/fontmap_p.h
/usr/include/pangomm-1.4/pangomm/private/fontmetrics_p.h
/usr/include/pangomm-1.4/pangomm/private/fontset_p.h
/usr/include/pangomm-1.4/pangomm/private/glyph_p.h
/usr/include/pangomm-1.4/pangomm/private/glyphstring_p.h
/usr/include/pangomm-1.4/pangomm/private/item_p.h
/usr/include/pangomm-1.4/pangomm/private/language_p.h
/usr/include/pangomm-1.4/pangomm/private/layout_p.h
/usr/include/pangomm-1.4/pangomm/private/layoutiter_p.h
/usr/include/pangomm-1.4/pangomm/private/layoutline_p.h
/usr/include/pangomm-1.4/pangomm/private/layoutrun_p.h
/usr/include/pangomm-1.4/pangomm/private/rectangle_p.h
/usr/include/pangomm-1.4/pangomm/private/renderer_p.h
/usr/include/pangomm-1.4/pangomm/private/tabarray_p.h
/usr/include/pangomm-1.4/pangomm/rectangle.h
/usr/include/pangomm-1.4/pangomm/renderer.h
/usr/include/pangomm-1.4/pangomm/tabarray.h
/usr/include/pangomm-1.4/pangomm/types.h
/usr/include/pangomm-1.4/pangomm/wrap_init.h
/usr/lib64/libpangomm-1.4.so
/usr/lib64/pangomm-1.4/include/pangommconfig.h
/usr/lib64/pkgconfig/pangomm-1.4.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/pangomm-1.4/images/gtkmm_logo.gif
/usr/share/doc/pangomm-1.4/images/top.gif
/usr/share/doc/pangomm-1.4/reference/html/annotated.html
/usr/share/doc/pangomm-1.4/reference/html/bc_s.png
/usr/share/doc/pangomm-1.4/reference/html/bdwn.png
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Analysis-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Analysis.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1AttrColor-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1AttrColor.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1AttrColor__inherit__graph.png
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1AttrFloat-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1AttrFloat.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1AttrFloat__inherit__graph.png
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1AttrFontDesc-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1AttrFontDesc.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1AttrFontDesc__inherit__graph.png
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1AttrInt-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1AttrInt.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1AttrInt__inherit__graph.png
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1AttrIter-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1AttrIter.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1AttrLanguage-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1AttrLanguage.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1AttrLanguage__inherit__graph.png
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1AttrList-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1AttrList.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1AttrShape-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1AttrShape.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1AttrShape__inherit__graph.png
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1AttrString-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1AttrString.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1AttrString__inherit__graph.png
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Attribute-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Attribute.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Attribute__inherit__graph.png
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1CairoFontMap-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1CairoFontMap.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1CairoFontMap__inherit__graph.png
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Color-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Color.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Context-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Context.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Context__inherit__graph.png
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Coverage-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Coverage.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Font-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Font.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1FontDescription-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1FontDescription.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1FontFace-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1FontFace.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1FontFace__inherit__graph.png
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1FontFamily-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1FontFamily.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1FontFamily__inherit__graph.png
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1FontMap-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1FontMap.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1FontMap__inherit__graph.png
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1FontMetrics-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1FontMetrics.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Font__inherit__graph.png
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Fontset-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Fontset.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Fontset__inherit__graph.png
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1GlyphGeometry-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1GlyphGeometry.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1GlyphInfo-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1GlyphInfo.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1GlyphString-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1GlyphString.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Item-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Item.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Language-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Language.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Layout-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Layout.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1LayoutIter-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1LayoutIter.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1LayoutLine-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1LayoutLine.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1LayoutRun-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1LayoutRun.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Layout__inherit__graph.png
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Rectangle-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Rectangle.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Renderer-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Renderer.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1Renderer__inherit__graph.png
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1TabArray-members.html
/usr/share/doc/pangomm-1.4/reference/html/classPango_1_1TabArray.html
/usr/share/doc/pangomm-1.4/reference/html/classes.html
/usr/share/doc/pangomm-1.4/reference/html/closed.png
/usr/share/doc/pangomm-1.4/reference/html/deprecated.html
/usr/share/doc/pangomm-1.4/reference/html/dir_175784427b70f00f3fb8995d1114dcb0.html
/usr/share/doc/pangomm-1.4/reference/html/doc.png
/usr/share/doc/pangomm-1.4/reference/html/doxygen-extra.css
/usr/share/doc/pangomm-1.4/reference/html/doxygen.css
/usr/share/doc/pangomm-1.4/reference/html/doxygen.png
/usr/share/doc/pangomm-1.4/reference/html/dynsections.js
/usr/share/doc/pangomm-1.4/reference/html/folderclosed.png
/usr/share/doc/pangomm-1.4/reference/html/folderopen.png
/usr/share/doc/pangomm-1.4/reference/html/functions.html
/usr/share/doc/pangomm-1.4/reference/html/functions_0x7e.html
/usr/share/doc/pangomm-1.4/reference/html/functions_b.html
/usr/share/doc/pangomm-1.4/reference/html/functions_c.html
/usr/share/doc/pangomm-1.4/reference/html/functions_d.html
/usr/share/doc/pangomm-1.4/reference/html/functions_e.html
/usr/share/doc/pangomm-1.4/reference/html/functions_f.html
/usr/share/doc/pangomm-1.4/reference/html/functions_func.html
/usr/share/doc/pangomm-1.4/reference/html/functions_func_0x7e.html
/usr/share/doc/pangomm-1.4/reference/html/functions_func_b.html
/usr/share/doc/pangomm-1.4/reference/html/functions_func_c.html
/usr/share/doc/pangomm-1.4/reference/html/functions_func_d.html
/usr/share/doc/pangomm-1.4/reference/html/functions_func_e.html
/usr/share/doc/pangomm-1.4/reference/html/functions_func_f.html
/usr/share/doc/pangomm-1.4/reference/html/functions_func_g.html
/usr/share/doc/pangomm-1.4/reference/html/functions_func_h.html
/usr/share/doc/pangomm-1.4/reference/html/functions_func_i.html
/usr/share/doc/pangomm-1.4/reference/html/functions_func_l.html
/usr/share/doc/pangomm-1.4/reference/html/functions_func_m.html
/usr/share/doc/pangomm-1.4/reference/html/functions_func_n.html
/usr/share/doc/pangomm-1.4/reference/html/functions_func_o.html
/usr/share/doc/pangomm-1.4/reference/html/functions_func_p.html
/usr/share/doc/pangomm-1.4/reference/html/functions_func_r.html
/usr/share/doc/pangomm-1.4/reference/html/functions_func_s.html
/usr/share/doc/pangomm-1.4/reference/html/functions_func_t.html
/usr/share/doc/pangomm-1.4/reference/html/functions_func_u.html
/usr/share/doc/pangomm-1.4/reference/html/functions_func_w.html
/usr/share/doc/pangomm-1.4/reference/html/functions_func_x.html
/usr/share/doc/pangomm-1.4/reference/html/functions_g.html
/usr/share/doc/pangomm-1.4/reference/html/functions_h.html
/usr/share/doc/pangomm-1.4/reference/html/functions_i.html
/usr/share/doc/pangomm-1.4/reference/html/functions_l.html
/usr/share/doc/pangomm-1.4/reference/html/functions_m.html
/usr/share/doc/pangomm-1.4/reference/html/functions_n.html
/usr/share/doc/pangomm-1.4/reference/html/functions_o.html
/usr/share/doc/pangomm-1.4/reference/html/functions_p.html
/usr/share/doc/pangomm-1.4/reference/html/functions_r.html
/usr/share/doc/pangomm-1.4/reference/html/functions_s.html
/usr/share/doc/pangomm-1.4/reference/html/functions_t.html
/usr/share/doc/pangomm-1.4/reference/html/functions_type.html
/usr/share/doc/pangomm-1.4/reference/html/functions_u.html
/usr/share/doc/pangomm-1.4/reference/html/functions_vars.html
/usr/share/doc/pangomm-1.4/reference/html/functions_w.html
/usr/share/doc/pangomm-1.4/reference/html/functions_x.html
/usr/share/doc/pangomm-1.4/reference/html/graph_legend.html
/usr/share/doc/pangomm-1.4/reference/html/graph_legend.png
/usr/share/doc/pangomm-1.4/reference/html/group__pangommEnums.html
/usr/share/doc/pangomm-1.4/reference/html/hierarchy.html
/usr/share/doc/pangomm-1.4/reference/html/index.html
/usr/share/doc/pangomm-1.4/reference/html/inherit_graph_0.png
/usr/share/doc/pangomm-1.4/reference/html/inherit_graph_1.png
/usr/share/doc/pangomm-1.4/reference/html/inherit_graph_10.png
/usr/share/doc/pangomm-1.4/reference/html/inherit_graph_11.png
/usr/share/doc/pangomm-1.4/reference/html/inherit_graph_12.png
/usr/share/doc/pangomm-1.4/reference/html/inherit_graph_13.png
/usr/share/doc/pangomm-1.4/reference/html/inherit_graph_14.png
/usr/share/doc/pangomm-1.4/reference/html/inherit_graph_15.png
/usr/share/doc/pangomm-1.4/reference/html/inherit_graph_16.png
/usr/share/doc/pangomm-1.4/reference/html/inherit_graph_17.png
/usr/share/doc/pangomm-1.4/reference/html/inherit_graph_18.png
/usr/share/doc/pangomm-1.4/reference/html/inherit_graph_19.png
/usr/share/doc/pangomm-1.4/reference/html/inherit_graph_2.png
/usr/share/doc/pangomm-1.4/reference/html/inherit_graph_20.png
/usr/share/doc/pangomm-1.4/reference/html/inherit_graph_21.png
/usr/share/doc/pangomm-1.4/reference/html/inherit_graph_3.png
/usr/share/doc/pangomm-1.4/reference/html/inherit_graph_4.png
/usr/share/doc/pangomm-1.4/reference/html/inherit_graph_5.png
/usr/share/doc/pangomm-1.4/reference/html/inherit_graph_6.png
/usr/share/doc/pangomm-1.4/reference/html/inherit_graph_7.png
/usr/share/doc/pangomm-1.4/reference/html/inherit_graph_8.png
/usr/share/doc/pangomm-1.4/reference/html/inherit_graph_9.png
/usr/share/doc/pangomm-1.4/reference/html/inherits.html
/usr/share/doc/pangomm-1.4/reference/html/jquery.js
/usr/share/doc/pangomm-1.4/reference/html/menu.js
/usr/share/doc/pangomm-1.4/reference/html/menudata.js
/usr/share/doc/pangomm-1.4/reference/html/modules.html
/usr/share/doc/pangomm-1.4/reference/html/namespaceGlib.html
/usr/share/doc/pangomm-1.4/reference/html/namespacePango.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_c.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_d.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_e.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_enum.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_eval.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_eval_c.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_eval_d.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_eval_e.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_eval_f.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_eval_g.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_eval_r.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_eval_s.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_eval_t.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_eval_u.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_eval_v.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_eval_w.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_f.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_func.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_g.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_i.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_l.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_m.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_o.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_r.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_s.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_t.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_type.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_u.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_v.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_vars.html
/usr/share/doc/pangomm-1.4/reference/html/namespacemembers_w.html
/usr/share/doc/pangomm-1.4/reference/html/namespaces.html
/usr/share/doc/pangomm-1.4/reference/html/nav_f.png
/usr/share/doc/pangomm-1.4/reference/html/nav_g.png
/usr/share/doc/pangomm-1.4/reference/html/nav_h.png
/usr/share/doc/pangomm-1.4/reference/html/open.png
/usr/share/doc/pangomm-1.4/reference/html/pages.html
/usr/share/doc/pangomm-1.4/reference/html/since_1_10.html
/usr/share/doc/pangomm-1.4/reference/html/since_1_14.html
/usr/share/doc/pangomm-1.4/reference/html/since_1_16.html
/usr/share/doc/pangomm-1.4/reference/html/since_1_18.html
/usr/share/doc/pangomm-1.4/reference/html/since_1_20.html
/usr/share/doc/pangomm-1.4/reference/html/since_1_20_1.html
/usr/share/doc/pangomm-1.4/reference/html/since_1_22.html
/usr/share/doc/pangomm-1.4/reference/html/since_1_30.html
/usr/share/doc/pangomm-1.4/reference/html/since_1_32.html
/usr/share/doc/pangomm-1.4/reference/html/since_1_32_4.html
/usr/share/doc/pangomm-1.4/reference/html/since_1_38.html
/usr/share/doc/pangomm-1.4/reference/html/since_1_4.html
/usr/share/doc/pangomm-1.4/reference/html/since_1_40.html
/usr/share/doc/pangomm-1.4/reference/html/since_1_42.html
/usr/share/doc/pangomm-1.4/reference/html/since_1_6.html
/usr/share/doc/pangomm-1.4/reference/html/since_1_8.html
/usr/share/doc/pangomm-1.4/reference/html/since_2_14.html
/usr/share/doc/pangomm-1.4/reference/html/since_2_16.html
/usr/share/doc/pangomm-1.4/reference/html/since_2_28.html
/usr/share/doc/pangomm-1.4/reference/html/since_2_42.html
/usr/share/doc/pangomm-1.4/reference/html/splitbar.png
/usr/share/doc/pangomm-1.4/reference/html/structPango_1_1AttributeTraits-members.html
/usr/share/doc/pangomm-1.4/reference/html/structPango_1_1AttributeTraits.html
/usr/share/doc/pangomm-1.4/reference/html/structPango_1_1ItemTraits-members.html
/usr/share/doc/pangomm-1.4/reference/html/structPango_1_1ItemTraits.html
/usr/share/doc/pangomm-1.4/reference/html/structPango_1_1LayoutLineTraits-members.html
/usr/share/doc/pangomm-1.4/reference/html/structPango_1_1LayoutLineTraits.html
/usr/share/doc/pangomm-1.4/reference/html/sync_off.png
/usr/share/doc/pangomm-1.4/reference/html/sync_on.png
/usr/share/doc/pangomm-1.4/reference/html/tab_a.png
/usr/share/doc/pangomm-1.4/reference/html/tab_b.png
/usr/share/doc/pangomm-1.4/reference/html/tab_h.png
/usr/share/doc/pangomm-1.4/reference/html/tab_s.png
/usr/share/doc/pangomm-1.4/reference/html/tabs.css
/usr/share/doc/pangomm-1.4/reference/pangomm-1.4.tag

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpangomm-1.4.so.1
/usr/lib64/libpangomm-1.4.so.1.0.30

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pangomm/COPYING
/usr/share/package-licenses/pangomm/COPYING.tools
