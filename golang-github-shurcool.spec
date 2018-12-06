# Run tests in check section
%bcond_without check

%global goipath         github.com/shurcooL/go
%global commit          47fa5b7ceee66c60ac3a281416089035bf526a3c

%global common_description %{expand:
Common Go code.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Common Go code
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/gopherjs/gopherjs/js)
BuildRequires: golang(github.com/shurcooL/github_flavored_markdown)
BuildRequires: golang(github.com/shurcooL/github_flavored_markdown/gfmstyle)
BuildRequires: golang(github.com/shurcooL/httpfs/vfsutil)
BuildRequires: golang(golang.org/x/tools/go/buildutil)
BuildRequires: golang(golang.org/x/tools/godoc/vfs)
BuildRequires: golang(golang.org/x/tools/refactor/importgraph)
BuildRequires: golang(gopkg.in/pipe.v2)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git47fa5b7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180419git47fa5b7
- First package for Fedora

