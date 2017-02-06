import os
from shutil import move, copy2
class SampleFileIO(object):
    topdir = ""

    def logerr(logpath, errlist, act):
        loghead = 'List of files that produced errors when attempting to %s:\n\n' % act
        logbody = '\n'.join(errlist)

        with open(logpath, 'w') as log:
            log.write(loghead + logbody)


    # Moving results
    def batchmove(results, dest, errlog=None):
        # List of results that produce errors
        errors = []

        # Make sure dest is a directory!
        if os.path.isfile(dest):
            print("The move destination '%s' already exists as a file!" % dest)
            exit(input('Press enter to exit...'))
        elif not os.path.isdir(dest):
            try:
                os.mkdir(dest)
            except:
                print("Unable to create '%s' folder!" % dest)
                exit(input('Press enter to exit...'))
            else:
                print("'%s' folder created" % dest)

        # Loop through results, moving every file to dest directory
        for paths in results.values():
            for path in paths:
                path = os.path.realpath(path)
                try:
                    # move file to dest
                    move(path, dest)
                except:
                    errors.append(path)
        print('File move complete')

        # log errors, if any
        if errlog and errors:
            logerr(errlog, errors, 'move')
            print("Check '%s' for errors." % errlog)
        exit(input('Press enter to exit...'))


    # Copying results
    def batchcopy(results, dest, errlog=None):
        # List of results that produce errors
        errors = []

        # Make sure dest is a directory!
        if os.path.isfile(dest):
            print("The copy destination '%s' already exists as a file!" % dest)
            exit(input('Press enter to exit...'))
        elif not os.path.isdir(dest):
            try:
                os.mkdir(dest)
            except:
                print("Unable to create '%s' folder!" % dest)
                exit(input('Press enter to exit...'))
            else:
                print("'%s' folder created" % dest)

        # Loop thru results, copying every file to dest directory
        for paths in results.values():
            for path in paths:
                path = os.path.realpath(path)
                try:
                    # copy file to dest
                    copy2(path, dest)
                except:
                    errors.append(path)
        print('File copying complete')

        # Log errors, if any
        if errlog and errors:
            logerr(errlog, errors, 'copy')
        exit(input('Press enter to exit...'))


    # Deleting results -- USE WITH CAUTION!
    def batchdel(results, errlog=None):
        # List of results that produce errors
        errors = []

        # Loop thru results, DELETING every file!
        for paths in results.values():
            for path in paths:
                path = os.path.realpath(path)
                try:
                    # Delete file
                    os.remove(path)
                except:
                    errors.append(path)
        print('File deletion complete')

        # Log errors, if any
        if errlog and errors:
            logerr(errlog, errors, 'delete')
        exit(input('Press enter to exit...'))


    # Logging results for findfile
    def logres(logpath, results):
        # The header in our logfile
        loghead = 'Search log from filefind for files in {}\n\n'.format(
            os.path.realpath(topdir))

        # The body of our log file
        logbody = ''

        # Loop through results
        for searchResult in results:
            # Concatenate the result from the results dict
            logbody += "<< Results with the extension '%s' >>" % searchResult
            logbody += '\n\n%s\n\n' % '\n'.join(results[searchResult])

        # write results to the logfile
        with open(logpath, 'w') as logfile:
            logfile.write(loghead)
            logfile.write(logbody)
