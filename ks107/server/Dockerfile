FROM microsoft/dotnet
WORKDIR ..

ADD ./server ./server
ADD ./app/build ./server/app/build 

WORKDIR ./server

RUN dotnet restore

RUN dotnet publish -c Release -o out

EXPOSE 5000

ENTRYPOINT ["dotnet", "out/server.dll"]
