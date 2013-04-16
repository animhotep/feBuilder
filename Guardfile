guard 'shell' do
  watch (%r{src/.+\.(html?)$}) do |m|
    `/usr/bin/python3.2 htmlInclude.py`
  end
end

guard 'compass' do
  watch(%r{src/sass/.+\.(scss)})
end

guard 'shell' do
  watch (%r{src/.+\.(js)}) do |m|
    `cat src/js/*.js > ./prod/js/all.js`
    #uncomment to compress
    #`java -jar ~/feBuilder/yuicompressor-2.4.8pre.jar ./prod/js/all.js -o ./prod/js/all.min.js && rm -rf ./prod/js/all.js`
  end
end

guard 'livereload' do
  watch(%r{prod/css/.+\.(css)})
  watch(%r{prod/.+\.(html?)$})
  watch(%r{prod/js/.+\.(js)})
end