
Name:		python-spiffgtkwidgets
Version:	0.2.0
Release:	1%{?dist}
License:	AGPLv3
Group:		Applications/System
Summary:	A collection of useful Gtk widgets
URL:		https://github.com/knipknap/SpiffGtkWidgets/
# Tarball can be obtained dynamically from GitHub. However, no tagged (fixed)
# package exists yet AFAIK.
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python, python-setuptools
BuildRequires:	pygtk2-devel
BuildRequires:	python2-devel
Requires:	pygtk2
Requires:       pygobject2
Requires:	hippo-canvas-python

%description
This library is part of the Spiff platform.

Spiff Gtk Widgets contains a number of Gtk widgets
by other Spiff components:

* A calendar similar to Google's online calendar.
* A text view that supports advanced features like undo/redo, annotations,
auto-indenting bullet point lists, etc.


%prep
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

%changelog
