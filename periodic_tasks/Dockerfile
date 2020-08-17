FROM ubuntu:latest

# Add crontab file in the cron directory
ADD crontab /etc/cron.d/periodic-tasks
ADD update_status.sh /home/

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/periodic-tasks
RUN chmod +x /home/update_status.sh

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

#Install Cron
RUN apt-get update
RUN apt-get -y install cron wget

# Run the command on container startup
CMD cron -f
