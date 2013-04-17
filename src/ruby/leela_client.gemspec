# -*- encoding: utf-8; mode: ruby -*-
require File.expand_path('../leela_client/version', __FILE__)

Gem::Specification.new do |gem|
  gem.authors       = ["PotHix", "dgvncsz0f"]
  gem.email         = ["pothix@pothix.com", "dsouza@c0d3.xxx"]
  gem.description   = %q{A client for leela server}
  gem.summary       = gem.description
  gem.homepage      = "https://github.com/locaweb/leela-client"

  gem.files         = Dir["./**/*"].reject {|file| file =~ /\.git|pkg|spec/}
  gem.require_paths = ["leela_client"]

  gem.name          = "leela_client"
  gem.version       = LeelaClient::VERSION
end
