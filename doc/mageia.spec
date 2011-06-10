%define git_repo SpiffGtkWidgets
%define git_head HEAD

Name:		python-spiffgtkwidgets
Version:	%git_get_ver
Release:	%mkrel %git_get_rel
License:	AGPLv3
Group:		Applications/System
Summary:	A collection of useful Gtk widgets
URL:		https://github.com/knipknap/SpiffGtkWidgets/
# Tarball can be obtained dynamically from GitHub. However, no tagged (fixed)
# package exists yet AFAIK.
Source0:	%git_bs_source %{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python, python-setuptools
BuildRequires:	pygtk2.0-devel
Requires:	pygtk2.0
Requires:	python-hippo-canvas

%description
This library is part of the Spiff platform.

Spiff Gtk Widgets contains a number of Gtk widgets
by other Spiff components:

* A calendar similar to Google's online calendar.
* A text view that supports advanced features like undo/redo, annotations,
auto-indenting bullet point lists, etc.


%prep
%git_get_source
%setup -q

%build

%{__python} ./setup.py build --quiet

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%{__python} ./setup.py install --root=%{buildroot} --quiet

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL README
%{python_sitelib}/SpiffGtkWidgets/
%{python_sitelib}/SpiffGtkWidgets-%{version}-py%{python_version}.egg-info

%changelog -f %{_sourcedir}/%{name}-changelog.gitrpm.txt
