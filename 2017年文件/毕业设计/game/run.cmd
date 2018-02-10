@echo off
for %%i in (%0) do set aa=%%~dpi 
cd %aa%
for %%i in (%1) do set aa=%%~dpi  
cd %aa%   
 
start   %~n1
