docker run --rm \
	--name pgdocker \
	-e POSTGRES_PASSWORD=password \
	-e POSTGRES_USER=postgres \
	-e POSTGRES_DB=database \
	-d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data postgres
