# CloudBackup Manager

Centralized backup management and monitoring platform for Linux servers.

CloudBackup Manager is a DevOps portfolio project designed to automate
backup operations across multiple Linux servers, store backup archives
in S3-compatible storage, verify data integrity, and monitor backup status.

## Project Goals

- Centralized management of Linux server backups
- Automated backup creation and upload
- SHA-256 integrity verification
- Configurable backup retention policies
- Backup status monitoring
- Telegram notifications
- Infrastructure monitoring with Prometheus and Grafana
- Containerized deployment using Docker Compose

## Planned Architecture

- Backend API: Python, FastAPI
- Database: PostgreSQL
- Backup Agent: Python
- Object Storage: S3-compatible storage
- AWS Integration: AWS API emulator for local development and testing
- Monitoring: Prometheus and Grafana
- Deployment: Docker Compose
- CI/CD: GitHub Actions

## Planned Features

1. Server and agent registration
2. Backup job management
3. Automated archive generation
4. Backup upload to object storage
5. SHA-256 integrity verification
6. Backup history and status tracking
7. Retention policy management
8. Monitoring dashboard
9. Telegram notifications

## Development Roadmap

- [ ] Infrastructure preparation
- [ ] Local AWS API emulator setup
- [ ] S3 storage integration
- [ ] DynamoDB integration
- [ ] Backend API development
- [ ] PostgreSQL integration
- [ ] Linux Backup Agent development
- [ ] Monitoring and alerting
- [ ] Docker Compose deployment
- [ ] CI/CD with GitHub Actions
- [ ] Documentation and testing

## Project Status

Work in progress. Features listed above are planned and will be
implemented incrementally.

## License

MIT
