{ pkgs ? import <nixpkgs> { } }:
let
  py = pkgs.python311;
  catppuccin-py = (
      py.pkgs.buildPythonPackage rec {
        pname = "catppuccin";
        version = "1.2.0";
        src = pkgs.fetchPypi {
          inherit pname version;
          sha256 = "sha256-hUNt6RHntQzamDX1SdhBzSj3pR/xxb6lpwzvYnqwOIo=";
        };
        doCheck = false;
        propagatedBuildInputs = [ ];
      }
    );
in
pkgs.mkShell {
  name = "python-shell";
  buildInputs = [
    py
    py.pkgs.setuptools
    catppuccin-py
  ];
}