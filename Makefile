non_container_dev:
	docker-compose -f dev/components.yaml up

docker-code-lint:
	echo "Checking Codestyle"
	docker run --rm -v ${CURDIR}:/data cytopia/black --check .
