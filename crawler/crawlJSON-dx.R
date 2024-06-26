library(tidyverse)
library(here)

#set working directory
setwd("C:/Users/Administrator/Documents/web_scarping/Nextbike")

## fix execution times
stop.date.time = as.POSIXct(format("2024-09-30 23:59:00 CEST", tz = "CET", usetz = TRUE)) # time of last execution
NOW = as.POSIXct(format(Sys.time(), tz = "CET", usetz = TRUE))
lapse.time = 60 # crawl data every 60s
exec.times = rev(seq(stop.date.time, NOW, -lapse.time))

## start at midnight of April 05, 2024
exec.times = exec.times[exec.times >= "2024-04-05 00:00:00 CEST"]

wait.time.for.errors = 5L

for (i in seq_along(exec.times)) {
  exec.time = exec.times[i]
  exec.name = gsub(":|[CEST]|[ ]", "-", exec.time)
  wait.time = difftime(exec.time, as.POSIXct(format(Sys.time(), tz = "CET", usetz = TRUE)), units = "secs") # calc difference in seconds
  if (wait.time > 0) {
    cat("\nWaiting", wait.time, "seconds before next execution\n")
    Sys.sleep(wait.time)
  }
  cat(as.character(as.POSIXct(format(Sys.time(), tz = "CET", usetz = TRUE))))
  
  ## download JSON file in a temporary file
#  if (!dir.exists("/json/dx/")) {
#    dir.create("/json/dx/")
#  }
  json.filename = sprintf("C:/Users/Administrator/Documents/web_scarping/Nextbike/dump/%s.json", exec.name)
  while (TRUE) {
    download.status = try(download.file(url = "https://nextbike.net/maps/nextbike-live.json?domains=dx", destfile = json.filename))
    if (!inherits(download.status, "try-error")) {
      break
    } else {
      download.status.api = try(download.file(url = "https://api.nextbike.net/maps/nextbike-live.json?domains=dx", destfile = json.filename))
      if (!inherits(download.status.api, "try-error")) {
        break
      } else {
        cat("\nEncountered a download error... Waiting", wait.time.for.errors, "seconds before next try\n")
        Sys.sleep(wait.time.for.errors)
      }
    }
  }
}

list.files()
list.dirs()
