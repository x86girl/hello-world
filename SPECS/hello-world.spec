Name:           hello-world
Version:        0.0
Release:        1%{?dist}
Summary:        A simple hello world written in C.

License:        MIT
URL:            https://github.com/x86girl/hello-world
Source0:        https://github.com/x86girl/hello-world/archive/refs/tags/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
This is just a simple example to show how to create a spec file for a C program.

%prep
%setup -q

%build
make %{?_smp_mflags}
%make_install

%changelog
* Tue Sep 05 2023 Priscila Gutierres <priscila.gutierres@gmail.com>
- 
