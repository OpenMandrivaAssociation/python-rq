Name:		python-rq
Version:	2.6.1
Release:	1
Summary:	RQ is a simple, lightweight, library for creating background jobs, and
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://pypi.org/project/rq/
Source0:	rq-2.6.1.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(click)
BuildRequires:	python%{pyver}dist(croniter)
BuildRequires:	python%{pyver}dist(redis)
BuildArch:	noarch
%description
RQ is a simple, lightweight, library for creating background jobs, and.

%files
%{py_sitedir}/*
%{_bindir}/*
