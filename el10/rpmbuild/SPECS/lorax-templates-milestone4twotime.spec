Name:           lorax-templates-milestone4twotime
Version:        1.0
Release:        1%{?dist}
Summary:        Milestone4TwoTime x86_v2 Lorax compatibility template
License:        GPL-2.0-or-later
BuildArch:      noarch
Requires:       lorax

Source0:        x86_v2.tmpl

%description
Provides the x86_v2 template name expected by Lorax on AlmaLinux 10.
The template delegates rendering to the installed x86_64 Lorax template.

%prep
%setup -q -c -T
cp %{SOURCE0} x86_v2.tmpl

%build

%install
install -Dpm 0644 x86_v2.tmpl \\
    %{buildroot}%{_datadir}/lorax/templates.d/80-rhel/x86_v2.tmpl

%files
%{_datadir}/lorax/templates.d/80-rhel/x86_v2.tmpl

%changelog
* Tue Nov 17 2026 Milestone4TwoTime <twotime@localhost.localdomain> - 1.0-1
- Add x86_v2 Lorax compatibility template
