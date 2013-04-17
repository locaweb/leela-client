# -*- encoding: utf-8 -*-
require File.expand_path('../lib/leela_client/version', __FILE__)

Gem::Specification.new do |gem|
  gem.authors       = ["PotHix", "dgvncsz0f"]
  gem.email         = ["pothix@pothix.com", "dgvncsz0f@bitforest.com"]
  gem.description   = %q{A client for leela chart server}
  gem.summary       = gem.description
  gem.homepage      = "https://github.com/locaweb/leela-client"

  gem.files         = Dir["./**/*"].reject {|file| file =~ /\.git|pkg/}
  gem.require_paths = ["lib"]

  gem.name          = "leela_client"
  gem.version       = LeelaClient::VERSION
end
