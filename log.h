// Copyright (c) 2011 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef BASE_LOGGING_H_
#define BASE_LOGGING_H_
#pragma once

//namespace logging {
#define DCHECK(x)    if (!(x)) std::cout << "Check failed"
#define CHECK(x)     if (!(x)) std::cout << "Check failed"
#define NOTREACHED()      std::cout << "Not reached"                                                                                       
#define DCHECK_EQ(x, y)   if ((x) != (y)) std::cout << "Check failed"
#define DCHECK_LE(x, y)   if ((x) > (y)) std::cout << "Check failed" 
#define DCHECK_GE(x, y)   if ((x) < (y)) std::cout << "Check failed" 
#define DCHECK_NE(x, y)   if ((x) == (y)) std::cout << "Check failed"
#define CHECK_NE(x, y)   if ((x) == (y)) std::cout << "Check failed"
//#define MAX(x,y)        ((x) > (y) ? (x) : (y))                                                                

#ifndef WARN_UNUSED_RESULT                                                                                                              
//#define WARN_UNUSED_RESULT
#endif

//}  // namespace base

#endif  // BASE_LOGGING_H_
